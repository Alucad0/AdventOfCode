def part_one(accessable, rolls):    
    for line_index in range(len(rolls)):
        for char_index in range(len(rolls[line_index])):
            # skip non "roll" element representations
            if rolls[line_index][char_index] != "@":
                continue
            if count_neighbors(rolls, line_index, char_index, target="@") < 4:
                accessable += 1

    return accessable


def part_two(total, rolls):
    accessable = True
    while accessable:
        removed = []

        for line_index in range(len(rolls)):
            for char_index in range(len(rolls[line_index])):
                if rolls[line_index][char_index] != "@":
                    continue
                
                count = count_neighbors(rolls, line_index, char_index, target="@")

                if count < 4:
                    removed.append((line_index, char_index))

        # no more to are able to be removed
        if removed == []:
            accessable = False
        else:
            total += len(removed)
            # remove the marked rolls
            for coord in removed:
                line_index, char_index = coord
                rolls[line_index] = rolls[line_index][:char_index] + "." + rolls[line_index][char_index+1:]
    return total


def parse_input(filepath):
    rolls = [line.removesuffix("\n") for line in open(filepath, "r").readlines()]
    return rolls



def count_neighbors(rolls, line_index, char_index, target="@"):
    """Count neighboring cells with the target character."""
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            # skip self
            if x == 0 and y == 0:
                continue
            new_x = char_index + x
            new_y = line_index + y
            # 
            if 0 <= new_x < len(rolls[line_index]) and 0 <= new_y < len(rolls):
                if rolls[new_y][new_x] == target:
                    count += 1
    return count



def main():
    data = parse_input("2025/ex_day4.txt")
    count = 0
    print(part_one(count, data))
    print(part_two(count, data))
    pass


if __name__ == "__main__":
    main()

