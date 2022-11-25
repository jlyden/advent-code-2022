"""https://adventofcode.com/2021/day/1"""

import pathlib

def part_one():
	input_file = pathlib.Path(__file__).parent.absolute() / 'input-01.txt'
	with open(input_file) as file:
		increases = 0
		previous = 0

		while True:
			line = file.readline()
			if not line:
				break
			current = int(line)
			if (current > previous):
				increases += 1
			previous = current

	# remove first increase (initial reading)
	increases -= 1
	return increases

print(part_one())

def part_two():
	input_file = pathlib.Path(__file__).parent.absolute() / 'input-01.txt'
	with open(input_file) as file:
		increases = 0
		contents = file.readlines()
		measurements = [int(value) for value in contents]
		length = len(measurements)

		previous = sum(measurements[0:3])

		# Stop when not enough measurements for sum of 3
		for i in range(1,length-2):
			current = sum(measurements[i:i+3])
			if (current > previous):
				increases += 1
			previous = current
	return increases

print(part_two())