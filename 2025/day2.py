def part_one(invalid_sums, ranges):
    for i in range(len(ranges)):
        ranges[i][0] = int(ranges[i][0])
        ranges[i][1] = int(ranges[i][1])
        
        for id in range(ranges[i][0], ranges[i][1] + 1):
            str_id = str(id)
            # if even and first half matches second half
            if len(str_id) % 2 == 0 and str_id[:len(str_id)//2] == str_id[len(str_id)//2:]:
                invalid_sums += id
    
    return invalid_sums

def part_two(invalid_sums, ranges):
    for i in range(len(ranges)):
        ranges[i][0] = int(ranges[i][0])
        ranges[i][1] = int(ranges[i][1])

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
                        invalid_sums += id
                        break
    return invalid_sums


def main():
    invalid_sum = 0
    ex_str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ranges =  [input_range.split("-") for input_range in ex_str.split(",")]

    result_part_one = part_one(invalid_sum, ranges)
    result_part_two = part_two(invalid_sum, ranges)

    print(f"Part One Result: {result_part_one}")
    print(f"Part Two Result: {result_part_two}")


if __name__ == "__main__":
    main()