"""https://adventofcode.com/2022/day/2

possible approaches
 - build evaluators for existing data - this file
 - transform data, then evaluate - alt coming soon
"""

from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-02.txt')

    if part == 'one':
        return sum([score_part_one_round(line) for line in lines]) 

    if part == 'two':
        return sum([score_part_two_round(line) for line in lines])

    raise Exception('What part are you trying to solve?')

"""Return second player score for round - based on part one info

round input looks like 'A Y\n'

not thrilled with this
 - could add '\n' to each round option to avoid str-replace, but ugly
 - could do more data transformation to handle outcomes algorithmically,
   but efficiency
"""
def score_part_one_round(raw_round):
    lose = ['B X', 'C Y', 'A Z']
    draw = ['A X', 'B Y', 'C Z']
    win = ['C X', 'A Y', 'B Z']

    round = raw_round.replace('\n','')
    if round in lose:
        return lose.index(round) + 1
    
    if round in draw:
        return draw.index(round) + 1 + 3

    if round in win:
        return win.index(round) + 1 + 6
    
    raise Exception('Invalid round: ' + round)

"""Return second player score for round - based on part two info

round input looks like 'A Y\n'
still not thrilled about approach
"""
def score_part_two_round(raw_round):
    round = raw_round.replace('\n','').split(' ')
    results_dict = {
        'X': ['B', 'C', 'A'],
        'Y': ['A', 'B', 'C'],
        'Z': ['C', 'A', 'B']
    }

    result_index = results_dict[round[1]].index(round[0])
    match round[1]:
        case 'X':
            return result_index  + 1
        case 'Y':
            return result_index + 1 + 3
        case 'Z':
            return result_index + 1 + 6
        case _:
            raise Exception('Invalid round result: ' + round)

print(runner('one'))
print(runner('two'))