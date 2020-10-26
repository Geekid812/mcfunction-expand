import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

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
    print(args)
    # Do something with args (WIP)

if __name__ == '__main__':
    main()