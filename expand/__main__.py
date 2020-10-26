import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter, FileType
from os import path

__version__ = '0.1.0'

def main():
    # Check for required version
    major = sys.version_info[0]
    minor = sys.version_info[1]
    micro = sys.version_info[2]

    python_version = f'{major}.{minor}.{micro}'
    version_string = f'mcfunction expand (Version {__version__})'

    if major < 3 or minor < 8:
        print(f'You are using Python {python_version}, however mcfunction expand requires Python 3.8+.\nPlease upgrade to a supported version of Python.')
        exit(1)

    # Parse command line arguments
    parser = ArgumentParser(prog='expand',formatter_class=RawDescriptionHelpFormatter,
    description=version_string)
    
    parser.add_argument('-w', '--watch', help='Start watching the current directory for file changes.', action='store_true')
    parser.add_argument('-v', '--version', help='Show this release\'s version number.', action='version', version=version_string)
    parser.add_argument('filename', help='Path to the file to compile.', default=None, nargs='?')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not any((args.filename, args.watch)):
        print('Error: No arguments provided. Use "expand --help" for help.')
        exit(1)
    
    if args.filename:
        # Check that the file provided is valid
        file_extension = path.splitext(args.filename)[1]
        if file_extension != '.mcfunction':
            print(f'Error: Can only compile files with extension \'.mcfunction\'.\nProvided file has extension \'{file_extension}\'.')
            exit(1)

        do_exit = False
        try:
            f = open(args.filename, 'r')
            f.close()
            del f

        except FileNotFoundError:
            print(f'Error: File \'{args.filename}\' does not exist.')
            exit(1)

        except IOError:
            print(f'Error: File \'{args.filename}\' is not accessible.')
            exit(1)
    
    # The input is validated, do something with it (WIP)

if __name__ == '__main__':
    main()