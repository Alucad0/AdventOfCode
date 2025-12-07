def part_one(total, numbers, operations):
    for column in range(len(operations)):
        op = operations[column]
        sub_total = 0
        for term in numbers[column]:
            term_value = int(''.join(term))
            match op:
                case "+":
                    sub_total += term_value
                case "*":
                    sub_total = 1 if sub_total == 0 else sub_total
                    sub_total *= term_value

        total += sub_total
    return total


def part_two(total, operations, grid_lines):
    problems = cephalopod_mapping(grid_lines, operations)
    
    for problem in problems:
        op = problem['op']
        terms = problem['terms']
        sub_total = 0
        
        for term_str in terms:
            term_value = int(term_str)
            match op:
                case "+":
                    sub_total += term_value
                case "*":
                    sub_total = 1 if sub_total == 0 else sub_total
                    sub_total *= term_value
        
        total += sub_total
    
    return total
    

def cephalopod_mapping(grid_lines, operators):
    """
    copilot auto-generated docstring:
    Parse cephalopod format by reading columns from right to left.
    Each non-empty column (looking only at the digit rows) is one operand:
    the column's characters, read top-to-bottom, form that operand's value.
    Empty columns separate problems. Operators are still listed left-to-right
    in the input, so we apply them in reverse order while scanning columns
    right-to-left.
    """
    max_len = max(len(line) for line in grid_lines)

    # pad all digit rows to the same length so column access is safe
    padded_lines = [line.ljust(max_len) for line in grid_lines]

    problems = []
    current_terms = []
    ops_reversed = list(reversed(operators))  # rightmost problem uses last operator
    op_idx = 0

    # scan columns from right to left
    for col_idx in range(max_len - 1, -1, -1):
        column_digits = ''.join(padded_lines[row][col_idx] for row in range(len(padded_lines)))
        stripped = column_digits.strip()

        if stripped:
            # the column is one operand (digits read top-to-bottom)
            current_terms.append(stripped)
        else:
            # empty column marks boundary between problems
            if current_terms:
                op = ops_reversed[op_idx] if op_idx < len(ops_reversed) else "+"
                problems.append({"op": op, "terms": current_terms})
                current_terms = []
                op_idx += 1

    # handle trailing problem (leftmost) if any terms remain
    if current_terms:
        op = ops_reversed[op_idx] if op_idx < len(ops_reversed) else "+"
        problems.append({"op": op, "terms": current_terms})

    return problems


def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]

    operator_line = lines[-1]
    data_lines = lines[:-1]
    
    # part one, parse normally (space-separated numbers)
    numbers = [' '.join(line.split()).split(" ") for line in data_lines]
    operands = [char for char in operator_line.replace(" ", "")]

    # part one, transpose the numbers as the operations are using the columns from the input_data
    part_one_data = transpose(numbers)
    
    # part two, we need the raw character grid to read columns
    #get the max line length to pad all lines
    max_len = max(len(line) for line in data_lines)
    padded_lines = [line.ljust(max_len) for line in data_lines]
    
    return part_one_data, operands, padded_lines


def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed


def main():
    total = 0
    filepath = "2025/ex_day6.txt"
    numbers, operations, grid_lines = parse_input(filepath)

    print(part_one(total, numbers, operations))
    print(part_two(total, operations, grid_lines))


if __name__ == "__main__":
    main()