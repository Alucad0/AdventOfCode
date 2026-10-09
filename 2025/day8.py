class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5


class Circuit:
    def __init__(self, points=[], size=0):
        self.points = points
        self.size = size

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

# fuckning msp (minimum spanning tree) based on the first dot
# probs not calc each edge dist and put it in a hashmap
    # n points -> n^2 edges -> O(n^2) to calc all edges


# 1. connect X junction boxes to circuits
    # connects thw two closest pts together to circuit
    # if two junctions already are in the same circuit, then skip

    # needs to be able to merge circuits
# 2. mult the 3 biggest circuits (sizes) together

def part_one(points):
    pass


def part_two(points):
    pass


def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    points = [Point(*map(int, line.split(","))) for line in lines]
    return points


def main():
    filepath = "2025/ex_day8.txt"
    points = parse_input(filepath)

    print("Part One:", part_one(points))
    print("Part Two:", part_two(points))


if __name__ == "__main__":
    main()