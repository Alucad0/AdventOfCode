def part_one(lines):
    pass

def part_two():
    pass


def parse_input(filepath):
    "just fkn make a compiler"
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    return lines


def main():
    filepath = "2024/ex_day4.txt"
    lines = parse_input(filepath)

    print(part_one(lines))
    # print(part_two(lines))



if __name__ == "__main__":
    main()