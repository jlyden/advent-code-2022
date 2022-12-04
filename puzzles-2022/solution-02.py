"""https://adventofcode.com/2022/day/2

possible approaches
 - build evaluators for existing data
 - transform data, then evaluate - alt coming soon
"""

from helpers import files

def runner(part):
    lines = files.get_contents_of_input_file('input-02.txt')

    if part == 'one':
        return sum([score_part_one_round(line) for line in lines]) 

    if part == 'two':
        return sum([score_part_two_round(line) for line in lines])
    
    if part == 'one-alt':
        return sum([score_part_one_round_alt(line) for line in lines])

    raise Exception('What part are you trying to solve?')

"""Return second player score for round - based on part one info

raw_round input looks like 'A Y\n'

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

raw_round input looks like 'A Y\n'
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

"""Return second player score for round - based on part one info

raw_round input looks like 'A Y\n'
"""
def score_part_one_round_alt(raw_round):
    moves = transform_round_to_int_list(raw_round)
    bonus = 0

    if player_two_win(moves):
        bonus = 6

    if draw(moves):
        bonus = 3

    # if not win or draw, no bonus
    return moves[1] + bonus

def transform_round_to_int_list(raw_round):
    moves = raw_round.replace('\n','').split(' ')
    return [map_move_to_value(move) for move in moves]

def map_move_to_value(move):
    match move:
        case 'A' | 'X':
            return 1
        case 'B' | 'Y':
            return 2
        case 'C' | 'Z':
            return 3
        case _:
            raise Exception('Invalid move: ' + move)

def draw(moves):
    return moves[0] == moves[1]

def player_two_win(moves):
    rock_beats_scissors = moves == [3,1]
    scissors_beats_rock = moves == [1,3]
    return rock_beats_scissors or (moves[0] < moves[1] and not scissors_beats_rock)

print(runner('one'))
print(runner('one-alt'))
print(runner('two'))