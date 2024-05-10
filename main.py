import os
import sys
import argparse
from termcolor import colored


FORMAT_FILE = 'Discovered open port {port}/tcp on {ip}'
ERROR_FORMAT_FILE = f'{colored('[-] The file must be in the following format: ', 'red', attrs=['bold'])} {FORMAT_FILE}'
ERROR_NUM_LINE: str = '[!] Line Error: {line_num}'

def check_exist_file(path_file: str) -> bool:
    """
        Check File Exists
    """
    return os.path.isfile(path_file)


def write_to_file(ip: list, port: str) -> None:
    """
        Write to File Result
    """
    try:
        with open('result/result.txt', 'a', encoding='utf-8') as f:
            for ip in ip:
                f.write('https://' + ip + ':' + port + '\n')
        print(colored('[+] Analysis completed successfully. Look at the result.txt file.', 'green', attrs=['bold']))
    except:
        print(colored('[-] An error occurred while writing to the file result.txt', 'red', attrs=['bold']))


def parse_file(path_file: str) -> None:
    """
        Parsing File
    """
    with open(path_file, 'r', encoding='utf-8') as f:
        lines: list[str] = f.readlines()
        ip_addr: list[str] = []
        port: str
        
        for idx, line in enumerate(lines):
            line: list[str] = line.strip().split(' ')
            # Check Format File
            if len(line) != 6:
                print(ERROR_FORMAT_FILE)
                print(colored(ERROR_NUM_LINE.format(line_num=idx + 1), 'yellow', attrs=['bold']))
                return
            if idx == 0:
                port = line[3].split('/')[0]
            ip_addr.append(line[5])
        
        # Save Result
        write_to_file(ip_addr, port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser Masscan Result File")
    parser.add_argument("-f", "--file", help="masscan result file", required=True)
    
    args = parser.parse_args()
    file: str = args.file
    
    # Check Exists file
    exist_file = check_exist_file(file)
    if not exist_file:
        print(colored('[-] File not found', 'red', attrs=['bold']))
        sys.exit()
    
    # Parsing File
    parse_file(file)
    
    

