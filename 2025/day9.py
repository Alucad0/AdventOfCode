def part_one(coords):
    """
    given coordinates of possible tile placements, create the 
    largest square such that two coords are oppossite of eachother
    """
    area = 0
    for corner in coords:
        for opposite in coords:
            if corner == opposite:
                continue
            # local area of rectangle with opposite corners
            local = (abs(corner[0] - opposite[0]) +1) * (abs(corner[1] - opposite[1]) +1)
            if local > area:
                area = local
    return area


def part_two(coords):
    """
    given a list of coordinates (red tiles) are used to encapsulate an area.
    green tiles are all of the tiles within the encaps area that aren't red. 
    what is the area of the largest rectangle that only contains red or green tiles. 
    """
    red_set = set(coords)
    red_list = list(coords)
    
    # the other shape (edge of the map)
    boundary_tiles = set(red_set)
    # connect consecutive red tiles
    for i in range(len(red_list)):
        current = red_list[i]
        next_red = red_list[(i + 1) % len(red_list)]
        
        if current[0] == next_red[0]:  # same row
            x = current[0]
            min_y, max_y = min(current[1], next_red[1]), max(current[1], next_red[1])
            for y in range(min_y, max_y + 1):
                boundary_tiles.add((x, y))
        elif current[1] == next_red[1]:  # same column
            y = current[1]
            min_x, max_x = min(current[0], next_red[0]), max(current[0], next_red[0])
            for x in range(min_x, max_x + 1):
                boundary_tiles.add((x, y))
    
    min_x = min(coord[0] for coord in boundary_tiles)
    max_x = max(coord[0] for coord in boundary_tiles)
    min_y = min(coord[1] for coord in boundary_tiles)
    max_y = max(coord[1] for coord in boundary_tiles)
    
    red_green_tiles = boundary_tiles.copy()
    
    # For each row, use ray casting to find interior points
    for y in range(min_y, max_y + 1):
        # Get all x values that have boundary tiles at this y
        xs_on_row = sorted(set(x for x, row_y in boundary_tiles if row_y == y))
        
        if len(xs_on_row) >= 2:
            # For interior detection, we count how many vertical boundary segments we cross
            # by checking if there are vertical segments ending/starting at adjacent y values
            for x in range(xs_on_row[0], xs_on_row[-1] + 1):
                if (x, y) in boundary_tiles:
                    continue
                
                # Count crossings to the right
                crossings = 0
                for check_x in xs_on_row:
                    if check_x > x:
                        # Check if there's a vertical segment at check_x crossing this row
                        # Look for (check_x, y-1) or (check_x, y+1) in boundary
                        if (check_x, y - 1) in boundary_tiles or (check_x, y + 1) in boundary_tiles:
                            crossings += 1
                
                if crossings % 2 == 1:
                    red_green_tiles.add((x, y))
    
    # Find the largest rectangle with red corners containing only red/green tiles
    max_area = 0
    
    for i, corner1 in enumerate(red_list):
        for j, corner2 in enumerate(red_list):
            if i == j:
                continue
            
            # Get the rectangle bounds
            x1, y1 = corner1
            x2, y2 = corner2
            min_x_rect, max_x_rect = min(x1, x2), max(x1, x2)
            min_y_rect, max_y_rect = min(y1, y2), max(y1, y2)
            
            # Check if all tiles in this rectangle are red or green
            valid = True
            for y in range(min_y_rect, max_y_rect + 1):
                for x in range(min_x_rect, max_x_rect + 1):
                    if (x, y) not in red_green_tiles:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                area = (max_x_rect - min_x_rect + 1) * (max_y_rect - min_y_rect + 1)
                if area > max_area:
                    max_area = area
    
    return max_area
    



def parse_input(filepath):
    lines = [line.rstrip("\n") for line in open(filepath, "r").readlines()]
    coords = [tuple(map(int, line.split(","))) for line in lines]
    return coords


def main():
    filepath = "2025/d9_input.txt"
    coords = parse_input(filepath)

    print("Part One:", part_one(coords))
    print("Part Two:", part_two(coords))


if __name__ == "__main__":
    main()