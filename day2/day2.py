'''

http://adventofcode.com/2018/day/2

'''

from collections import Counter

def read_input(input_file):
    with open(input_file) as f:                                                                                                                                                 
        content = f.readlines()
    
    return content

def part_1(input_list):
    cnt_2 = 0
    cnt_3 = 0

    for box_id in input_list:
        counts = Counter(box_id)
        if (2 in counts.values()):
            cnt_2 += 1
        if (3 in counts.values()):
            cnt_3 += 1
    
    return cnt_2 * cnt_3

def part_2_modify_word(word, index):
    return word[:index] + word[index+1:]

def part_2(input_list):
    modified_words = set()

    for word in input_list:
        word_len = len(word)

        # Ensure that we do not count modified words that
        # occur in the same word
        # e.g. abb -> ab, bb, ab
        curr_modified_words = set()

        for i in range(word_len):
            # Generate a list of modified words
            # where a letter is removed
            modified_word = part_2_modify_word(word, i)
            curr_modified_words.add(modified_word)

            if modified_word in modified_words:
                return modified_word

        for word in curr_modified_words:
            modified_words.add(word)
            

if __name__ == '__main__':
    INPUT_PATH = "input.txt"
    input_list = read_input("input.txt")

    print part_1(input_list)
    print part_2(input_list)
