#!/usr/bin/env python3
# Author ID: ssuresh14

def read_file_string(file_name):
    # Takes file_name as string, returns entire contents as a string
    with open(file_name, 'r') as f:
        content = f.read()
    return content

def read_file_list(file_name):
    # Takes file_name as string, returns list of lines WITHOUT new-line chars
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # Remove trailing '\n' from each line
    lines = [line.rstrip('\n') for line in lines]
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
