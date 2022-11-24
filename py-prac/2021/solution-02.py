"""Straightforward solution separating two problems"""
def part_one():
	with open('input-02.txt') as file:
		horz_pos = 0
		depth = 0

		while True:
			line = file.readline()
			if not line:
				break
			
			parts = line.split(' ')
			direction = parts[0]
			value = int(parts[1])

			match direction:
				case 'forward':
					horz_pos += value
				case 'down':
					depth += value
				case 'up':
					depth -= value
				case _:
					raise Exception('Invalid direction: ' + direction)
	
	return horz_pos * depth

print(part_one())

def part_two():
	with open('input-02.txt') as file:
		horz_pos = 0
		depth = 0
		aim = 0

		while True:
			line = file.readline()
			if not line:
				break
			
			parts = line.split(' ')
			direction = parts[0]
			value = int(parts[1])

			match direction:
				case 'forward':
					horz_pos += value
					depth += (aim * value)
				case 'down':
					aim += value
				case 'up':
					aim -= value
				case _:
					raise Exception('Invalid direction: ' + direction)
	
	return horz_pos * depth

print(part_two())