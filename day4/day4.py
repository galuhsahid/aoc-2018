'''

http://adventofcode.com/2018/day/4

'''

import re
import operator

def read_input(input_file):
    with open(input_file) as f:                                                                                                                                                 
        content = f.readlines()
    
    return content

def parse(entry):
    pattern = "\[[0-9]+-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (Guard #[0-9]+|falls asleep|wakes up)"
    result = re.match(pattern, entry).groups()

    return result

def part_1_2(entries):
    counter = {}

    for entry in entries:
        entry = parse(entry)

        if entry[4].startswith("Guard"):
            if entry[4] not in counter.keys():
                counter[entry[4]] = {}
            current_guard = entry[4]

        if entry[4] == "falls asleep":
            start = int(entry[3])
        
        if entry[4] == "wakes up":
            end = int(entry[3])

            for x in range(start, end):
                try:
                    counter[current_guard][x] += 1
                except:
                    counter[current_guard][x] = 1

    counter = {k:v for k,v in counter.items() if v != {}}

    guard_1 = max(counter, key=lambda k: sum(counter[k].values()))
    minute_1 = max(counter[guard_1].iteritems(), key=operator.itemgetter(1))[0]
    guard_1 = int(re.match("Guard #([0-9]+)", guard_1).groups()[0])

    guard_2 = max(counter, key=lambda k: max(counter[k].values()))
    minute_2 = max(counter[guard_2].iteritems(), key=operator.itemgetter(1))[0]
    guard_2 = int(re.match("Guard #([0-9]+)", guard_2).groups()[0])

    return guard_1 * minute_1, guard_2 * minute_2

if __name__ == '__main__':
    INPUT_PATH = "input.txt"
    input_list = read_input(INPUT_PATH)
    input_list = sorted(input_list)
    
    part_1, part_2 = part_1_2(input_list)
    print part_1
    print part_2    
