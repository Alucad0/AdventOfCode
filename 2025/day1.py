def part_one(ptr, data):
    zero_counter = 0

    for line in data:
        line = line.removesuffix("\n")
        direction, value = line[0], int(line[1:])
        
        if direction == "L":
            ptr = ptr - value
            ptr = ptr % 100
        elif direction == "R":
            ptr = ptr + value
            ptr = ptr % 100

        if ptr == 0:
            zero_counter += 1
    
    return zero_counter


def part_two(ptr, data):
    zero_tick_counter = 0
    for line in data:
        line = line.strip()
        direction, value = line[0], int(line[1:])
        ops = 0
        if direction == "R":
            ops = (ptr + value) // 100
            ptr = (ptr + value) % 100
        else:  # "L"
            if ptr == 0:
                ops = value // 100
            elif value < ptr:
                ops = 0
            else:
                ops = (value - ptr) // 100 + 1
            ptr = (ptr - value) % 100

        zero_tick_counter += ops
        
    return zero_tick_counter


def parse_input(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines



def main():
    start_ptr = 50
    input_data = parse_input("2025/ex_day1.txt")

    result_part_one = part_one(start_ptr, input_data)
    result_part_two = part_two(start_ptr, input_data)

    print(f"Part One Result: {result_part_one}")
    print(f"Part Two Result: {result_part_two}")


if __name__ == "__main__":
    main()