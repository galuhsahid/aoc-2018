'''

http://adventofcode.com/2018/day/5

'''

def read_input(input_file):
    with open(input_file) as f:                                                                                                                                                 
        content = [line.rstrip() for line in f.readlines()] 
    
    return content

def part_1(polymer):
    polymer = list(polymer)
    stack = []

    for char in polymer:
        if stack and (stack[-1] == char.swapcase()):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

def part_2(polymer):
    chars = set([x.lower() for x in polymer])
    counter = {}

    return min([part_1(polymer.replace(char, "").replace(char.upper(), "")) for char in chars])


if __name__ == '__main__':
    INPUT_PATH = "input.txt"
    polymer = read_input(INPUT_PATH)[0]

    print part_1(polymer)
    print part_2(polymer)
