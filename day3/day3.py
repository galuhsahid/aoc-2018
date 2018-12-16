'''

http://adventofcode.com/2018/day/3

'''

def read_input(input_file):
    with open(input_file) as f:                                                                                                                                                 
        content = f.readlines()
    
    return content

def parse(claim):
    parsed = claim.split(" ")
    claim_id = parsed[0]
    loc = parsed[2].split(",")
    area = parsed[3].split("x")

    left = int(loc[0])
    top = int(loc[1].replace(":", ""))
    width = int(area[0])
    height = int(area[1])

    return claim_id, left, top, width, height

def part_1(claim_list):
    all_coords = {}
    sq_inch = 0

    for claim in claim_list:
        _, left, top, width, height = parse(claim)

        for row in range(1, height+1):
            for col in range(1, width+1):
                try:
                    x = (row+top)
                    y = (col+left)
                    all_coords[x,y] += 1
                    if all_coords[x,y] == 2:
                        sq_inch += 1
                except:
                    all_coords[x,y] = 1
    
    return sq_inch

def part_2(claim_list):
    all_coords = {}

    for claim in claim_list:
        claim_id, left, top, width, height = parse(claim)

        for row in range(1, height+1):
            for col in range(1, width+1):
                x = (row+top)
                y = (col+left)
                
                try:
                    all_coords[x, y] += 1
                except:
                    all_coords[x, y] = 1
    
    overlap_coords = set(k for k, v in all_coords.items() if v > 1)
    
    for claim in claim_list:
        claim_id, left, top, width, height = parse(claim)
        claim_coords = set()

        for row in range(1, height+1):
            for col in range(1, width+1):
                x = (row+top)
                y = (col+left)
                
                claim_coords.add((x, y))

        if len(claim_coords) == len(claim_coords - overlap_coords):
            return claim_id

if __name__ == '__main__':
    INPUT_PATH = "input.txt"
    input_list = read_input("input.txt")

    print part_1(input_list)
    print part_2(input_list)

