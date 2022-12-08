"""https://adventofcode.com/2022/day/7"""

import re
from helpers import files

def part_one(dir_size_limit):
    lines = files.get_contents_of_input_file('input-mini-mini.txt')
    dir_structure = build_directory_structure(lines)
    requested_sizes = get_dir_sizes(dir_structure, [])
    return sum(requested_sizes)

def build_directory_structure(lines):
    pwd = []
    dirs = []
    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        line_type = evaluate_line_type(line)
        match line_type:
            case 'cd':
                pwd.append(line.split(' ')[2])
            case 'ls':
                dirs.append({})
            case 'dir_name':
                dir_name = line.split(' ')[1]
                dirs[-1].update({dir_name: {}})
            case 'file_name':
                [size, file_name] = line.split(' ')
                dirs[-1].update({file_name: int(size)})
            case 'cd_back':
                subdir = dirs.pop()
                dirs[-1].update({pwd[-1]: subdir})
                pwd.pop()
    if len(pwd) > 1:
        subdir = dirs.pop()
        dirs[-1].update({pwd[-1]: subdir})
    if len(dirs) > 1:
        raise Exception('Weird, muliple dicts in dirs: ' + str(dirs))
    return dirs[0]

def evaluate_line_type(line):
    type = ''
    if line == '$ cd ..':
        type = 'cd_back'
    elif line == '$ ls':
        type = 'ls'
    elif re.match('^\$ cd ', line):
        type = 'cd'
    elif re.match('^dir ', line):
        type = 'dir_name'
    elif re.match('^\d* \w', line):
        type = 'file_name'
    else:
        raise Exception('Unexpected line: ' + line)
    return type
    
# TODO: This is wrong, but I am tired
def get_dir_sizes(dir_structure, dir_sizes):
    print(str(dir_structure))
    for key, value in dir_structure.items():
        sum = 0
        print(key)
        print(value)
        if isinstance(value, dict):
            dir_sizes.append(sum)
            print(dir_sizes)
            return get_dir_sizes(dir_structure[key], dir_sizes)
        else:
            sum += value
    dir_sizes.append(sum)
    return dir_sizes

print(part_one(100000))