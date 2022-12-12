import pathlib

""" Returns list of strings, one string for each line of file_name

Hard coded for existing directory structure
"""
def get_contents_of_input_file(file_name):
    input_file = pathlib.Path(__file__).parents[1] / 'input' / file_name
    with open(input_file) as file:
        return file.readlines()
