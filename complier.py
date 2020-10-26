from re import search, compile
from collections.abc import Iterable

import math
import string

RE_EVAL_MATCH = compile(r'\*\([^*\n]+\)\*')
RE_ASSIGNMENT = compile(r'^(?P<var_name>\w+)( )?=( )?(?P<var_value>.+)$')


def compile_function(path):
    with open(path, 'r') as f:
        contents = f.read()
    lines = contents.split('\n')
    
    # Do not compile if file starts with '# NO-EXPAND'
    if contents.startswith('# NO-EXPAND'): return
    
    # --- EVALUATION ---
    evaluated = ''

    # A dictionnary which maps line numbers to arrays of iterables they contain
    iterables = {}

    current_pos = 0
    variables = {'math': math, 'string': string}
    while match := RE_EVAL_MATCH.search(contents, current_pos):
        evaluated += contents[current_pos : match.start()]

        current_pos = match.end()
        eval_content = match[0][2:-2]
        line_number = contents[:current_pos].count('\n')

        # Sanitizing the eval input
        eval_content = eval_content.replace('__import__','')
        eval_content = eval_content.replace('eval','')

        # Variable assignment
        if assignment := RE_ASSIGNMENT.match(eval_content):
            name = assignment.group('var_name')
            returned_value = eval(assignment.group('var_value'), variables)
            variables[name] = returned_value

        # Anything else
        else:
            returned_value = eval(eval_content, variables)

        # Save iterables for later (except strings)
        if isinstance(returned_value, Iterable) and type(returned_value) != str:
            if line_number not in iterables:
                iterables[line_number] = []
            index = len(iterables[line_number])
            iterables[line_number].append(list(returned_value))

            # Write a placeholder with the index so that we know where to write the values later
            evaluated += '*(' + str(index) + ')*'

        # Not an iterable, we can just write the returned value
        else:
            evaluated += str(returned_value)

    evaluated += contents[current_pos:]

    # --- EXPANDING ---
    out = ''
    lines = evaluated.split('\n')

    for line_number, line in enumerate(lines):
        # If there are no iterables to write, keep that line as is
        if line_number not in iterables:
            out += line + '\n'
            continue
        
        # Iterables in that line
        iters = iterables[line_number]

        # Determine how many lines we are going to write
        max_length = max([len(array) for array in iters])
        for i in range(max_length):

            # Replace the placeholders with the values (i as the iterable's index)
            format_line = line
            for placeholder_index, iterable in enumerate(iters):
                format_line = format_line.replace(f'*({placeholder_index})*',str(iterable[i % len(iterable)]))
            
            out += format_line + '\n'

    # Remove trailing newline
    out = out[:-1]

    # Write the output to the file
    with open(path, 'w') as f:
        f.write(out)
