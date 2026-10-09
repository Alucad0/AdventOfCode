def part_one(lines):
    unsafe_count = 0
    reports = []

    # parsing input again
    for line in lines:
        rep = []
        for numb in line.split(" "):
            rep.append(int(numb))
        reports.append(rep)

    for rep in reports:
        inc = False
        dec = False
        for idx in range(len(rep) - 1):
            diff = rep[idx] - rep[idx+1]
            if diff < 0: dec = True
            if diff > 0: inc = True
            diff = abs(diff)

            # adj check 
            if diff == 0 or not (3 >= diff or diff <= 1) or (inc and dec):
                unsafe_count += 1
                break

    return (len(lines) - unsafe_count)

def part_two():
    pass


def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    return lines


def main():
    filepath = "2024/d2_input.txt"
    lines = parse_input(filepath)

    print(part_one(lines)) # 369
    # print(part_two(lines))



if __name__ == "__main__":
    main()