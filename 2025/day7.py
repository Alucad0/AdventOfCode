def part_one(lines):
    beam_index = []
    split_counter = 0

    for line in lines:
        for char_index in range(len(line)):
            char = line[char_index]
            if char == "S":
                beam_index.append(char_index)

            # handle beam splitting
            if char == "^" and char_index in beam_index:
                beam_index.remove(char_index)
                split_counter += 1
                
                # as to not create duplicates
                if not (char_index - 1) in beam_index:
                    beam_index.append(char_index - 1)            
                if not (char_index + 1) in beam_index:
                    beam_index.append(char_index + 1)

    return split_counter


def part_two(lines):
    # count all possible paths a beam can take
    path_count = 0
    
    pass


def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    return lines


def main():
    filepath = "2025/ex_day7.txt"
    lines = parse_input(filepath)

    print(part_one(lines))
    print(part_two(lines))



if __name__ == "__main__":
    main()