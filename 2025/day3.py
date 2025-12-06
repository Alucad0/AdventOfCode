def part_one(power, joltage):
    for electricity in joltage:
        val = 0
        digit = 0
        for index in range(len(electricity)):
            
            if int(electricity[index]) > val and index != len(electricity) - 1:
                val = int(electricity[index])
                digit = 0  # reset digit when a new val is found
            
            elif int(electricity[index]) > digit:
                digit = int(electricity[index])

        power += val*10 + digit
    return power

def part_two(total, joltage):
    power_len = 12
    total = 0
    for electricity in joltage:
        digits = electricity
        n = len(digits)

        chosen = []
        start = 0

        # select power_len digits to form the largest number
        for pick in range(power_len):
            # the last searchable position to ensure that it will have enough digits left
            end = n - (power_len - pick)

            # find the largest digit in digits[start:end+1]
            max_digit = '0'
            max_index = start
            for i in range(start, end + 1):
                if digits[i] > max_digit:
                    max_digit = digits[i]
                    max_index = i

            chosen.append(max_digit)
            start = max_index + 1  # next search begins after the chosen digit

        total += int("".join(chosen))

    return total


def parse_input(filepath):
    lines = [line.removesuffix("\n") for line in open(filepath, "r").readlines()]
    return lines

def main():
    data = parse_input("2025/ex_day3.txt")
    power = 0
    print(part_one(power, data))
    print(part_two(0, data))


if __name__ == "__main__":
    main()

