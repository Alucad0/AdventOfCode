def day_one(): 
    # copy and paste ur input into a txt file 
    file_input = open("ex1.txt", "r")
    lines = file_input.readlines()
    file_input.close()
    
    ptr = 50
    
    def part_one(ptr, lines):
        count = 0
        for line in lines:
            line = line.removesuffix("\n")
            direction, value = line[0], int(line[1:])
            if direction == "L":
                ptr = ptr - value
                ptr = ptr % 100
            elif direction == "R":
                ptr = ptr + value
                ptr = ptr % 100
            
            # print(ptr)
            
        return count
    
    # counts how many times ptr goes past 0, i.e landing on or passing it
    def part_two(ptr, lines):
        count = 0
        for line in lines:
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

            count += ops
            print(f"ptr: {ptr}, ops: {ops}")

        return count



def day_two():
    ex_str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ranges =  [input_range.split("-") for input_range in ex_str.split(",")]

    def part_one(ranges):
        invalid_sums = 0
        for i in range(len(ranges)):
            ranges[i][0] = int(ranges[i][0])
            ranges[i][1] = int(ranges[i][1])
            # print(f"checking range: {ranges[i][0]} to {ranges[i][1]}")

            for id in range(ranges[i][0], ranges[i][1] + 1):
                str_id = str(id)
                # if even and first half matches second half
                if len(str_id) % 2 == 0 and str_id[:len(str_id)//2] == str_id[len(str_id)//2:]:
                    # print(f"invalid: {id}")
                    invalid_sums += id
        
        return invalid_sums

    def part_two(ranges):
        invalid_sums = 0
        for i in range(len(ranges)):
            ranges[i][0] = int(ranges[i][0])
            ranges[i][1] = int(ranges[i][1])
            # print(f"checking range: {ranges[i][0]} to {ranges[i][1]}")

            for id in range(ranges[i][0], ranges[i][1] + 1):
                str_id = str(id)
                # invalid if it is only made up of some sequence of digits rep at least twice
                length = len(str_id)

                # max sequence length is half the length of the string
                for seq_len in range(1, length // 2 + 1):
                    # is checkable
                    if length % seq_len == 0:
                        # cmp sequence repeated reps times to original string
                        seq = str_id[:seq_len]
                        reps = length // seq_len
                        if seq * reps == str_id:
                            # print(f"invalid: {id}")
                            invalid_sums += id
                            break
        return invalid_sums

    print(part_two(ranges))


def day_three():
    def part_one():
        joltage = [line.removesuffix("\n") for line in open("2025_ex_day3.txt", "r").readlines()]

        # print(joltage)
        power = 0
        for electricity in joltage:
            # gets the two largest values from electricity
            val = 0
            digit = 0
            for index in range(len(electricity)):
                
                if int(electricity[index]) > val and index != len(electricity) - 1:
                    val = int(electricity[index])
                    digit = 0  # reset digit when a new val is found
                
                elif int(electricity[index]) > digit:
                    digit = int(electricity[index])
                    
            # print(f"val: {val}, digit: {digit}")
            power += val*10 + digit

        return power

    def part_two():
        joltage = [line.removesuffix("\n") for line in open("2025_ex_day3.txt", "r")]
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

