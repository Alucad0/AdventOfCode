def part_one(lines):
    left = []
    right = []
    dist = 0
    
    # seperate input into two lists
    for line in lines:
        line.split(" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))
    
    # sorting is needed to match the smallest from each resp list
    left.sort()
    right.sort()

    for idx in range(len(lines)):
        dist += abs(left[idx] - right[idx])
        
    return dist

def part_two():
    pass


def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    return lines


def main():
    filepath = "2024/ex_day1.txt"
    lines = parse_input(filepath)

    "523"
    print(part_one(lines)) 
    # print(part_two(lines))



if __name__ == "__main__":
    main()