'''

http://adventofcode.com/2018/day/1

'''

def read_input(input_file):
    with open(input_file) as f:                                                                                                                                                 
        content = f.readlines()
        content = [int(x.replace("+", "")) for x in content]
    
    return content

def part_1(input_list):
    return sum(input_list)

def part_2(input_list):
    seen = set()
    counter = 0
    seen.add(counter)

    while True:
        for num in input_list:
            counter += num

            if counter in seen:
                return counter
            
            seen.add(counter)

if __name__ == '__main__':
    INPUT_PATH = "input.txt"
    input_list = read_input("input.txt")

    print part_1(input_list)
    print part_2(input_list)