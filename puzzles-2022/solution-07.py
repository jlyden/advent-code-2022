"""https://adventofcode.com/2022/day/7

Part One done
"""

import re
from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-07.txt')
    dir_structure = build_folded_directory_structure(lines)
    all_dir_sizes = get_dir_sizes(dir_structure, [])
    if part == 'one':
        return sum([size for size in all_dir_sizes if size <= 100000])
    return get_size_of_dir_to_delete(all_dir_sizes)

def get_size_of_dir_to_delete(all_dir_sizes):
    all_dir_sizes.sort()
    total_size = 70000000
    update_space_required = 30000000
    current_space_used = all_dir_sizes.pop()
    current_space_available = total_size - current_space_used
    open_space_still_needed = update_space_required - current_space_available
    # TODO: binary sort would be faster
    for dir_size in all_dir_sizes:
        if dir_size >= open_space_still_needed:
            return dir_size

def build_folded_directory_structure(lines):
    pwd = []
    dirs = []
    for untrimmed_line in lines:
        line = untrimmed_line.replace('\n', '')
        line_type = evaluate_line_type(line)
        match line_type:
            case 'cd':
                # '$ cd /'
                pwd.append(line.split(' ')[2])
            case 'ls':
                dirs.append({})
            case 'dir_name':
                # 'dir a'
                dir_name = line.split(' ')[1]
                dirs[-1].update({dir_name: {}})
            case 'file_name':
                # '14848514 b.txt'
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
    
def get_dir_sizes(dir_structure, dir_sizes):
    sum = 0
    for key, value in dir_structure.items():
        if isinstance(value, dict):
            get_dir_sizes(dir_structure[key], dir_sizes)
            last_subdir_size = dir_sizes[-1]
            sum += last_subdir_size
        else:
            sum += value
    dir_sizes.append(sum)
    return dir_sizes

#print(runner('one'))
print(runner('two'))