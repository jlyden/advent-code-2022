"""Build 2 dimensional array from 1-D string array"""
def build_two_d_int_array(lines):
    output = []
    for line in lines:
        digits = [int(x) for x in str(line) if x != '\n']
        output.append(digits)
    return output