def part_one(fresh, ingredients, available):
    for item_id in ingredients:
        for touple in available:
            lower, upper = touple
            # item fresh if within range for any available ingredient
            if lower <= int(item_id) <= upper:
                fresh += 1
                break

    return fresh

def part_two(total, ingredients_ranges):
    ingredients_ranges.sort()

    merged = []
    current_lo, current_hi = ingredients_ranges[0]

    for lo, hi in ingredients_ranges[1:]:
        # overlaping -> extend the current range
        if lo <= current_hi + 1:
            current_hi = max(current_hi, hi)
        else:
            # no overlap -> push current and start a new one
            merged.append((current_lo, current_hi))
            current_lo, current_hi = lo, hi

    merged.append((current_lo, current_hi))

    total = sum(hi - lo + 1 for lo, hi in merged)
    return total




def parrse_input(filepath):
    available = []
    ingredients = []
    swap = False
    for line in open(filepath, "r").readlines():
        line = line.removesuffix("\n")
        if line == "":
            swap = True
            continue
        if not swap:
            lower, upper = map(int, line.split("-"))
            available.append((lower, upper))
        else:
            ingredients.append(line)

    return available, ingredients
    


def main():
    count = 0
    available, ingredients = parrse_input("2025/ex_day5.txt")

    print(part_one(count, ingredients, available))
    print(part_two(count, available))
    


if __name__ == "__main__":
    main()
