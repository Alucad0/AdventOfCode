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
    # dynamic-programming pass row-by-row, tracking how many beams occupy each column
    start_row, start_col = next(
        (row_idx, line.index("S")) for row_idx, line in enumerate(lines) if "S" in line
    )

    column_counts = {start_col: 1}

    for row_idx in range(start_row + 1, len(lines)):
        line = lines[row_idx]
        next_counts = {}

        for col, count in column_counts.items():
            char = line[col] if 0 <= col < len(line) else "."
            if char == "^":
                # split left and right if still inside the grid
                for new_col in (col - 1, col + 1):
                    if 0 <= new_col < len(line):
                        next_counts[new_col] = next_counts.get(new_col, 0) + count
            else:
                next_counts[col] = next_counts.get(col, 0) + count

        column_counts = next_counts

    return sum(column_counts.values())


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