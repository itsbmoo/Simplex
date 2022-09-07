import os
import sys
import colorama
from colorama import Fore

colorama.init(True)


def error(line: int, code: str, msg: str) -> str:
    print(f'{Fore.RED}ERROR: {msg}')
    print(f'\t{line} | {code}')
        
    
def run_file(code: str) -> str:
    print(code)
    
def run_prompt() -> str:
    print('Prompt')


def usage() -> str:
    os.system('cls')
    print(f'{Fore.YELLOW}USAGE:\n\t> simplex.py \t\t- Run the prompt\n\t> simplex.py [filename] - Run the file')
    exit(0)
    
    
if __name__ == '__main__':
    os.system('cls')
    match len(sys.argv):
        case 1:
            run_prompt()
        case 2:
            try:
                f = open(sys.argv[1], 'r')
                run_file(f.read())
            except Exception as e:
                print(f'{Fore.RED}ERROR: {e}')
        case _:
            usage()