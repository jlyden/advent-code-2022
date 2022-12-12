"""Class representing a Monkey

https://adventofcode.com/2022/day/

items: array
worry_transform: string
worry_transform_value: int
test_value: int

TODO: write three static functions
 - add to
 - multiply by
 - divide by
"""

class Monkey:

    def __init__(self, items, worry_level_change, test):
        self.items = items
        self.worry_level_change = worry_level_change
        self.test = test