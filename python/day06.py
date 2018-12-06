from InputReader import read_input


def man_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_closest_points(coords, pos):
    min_dist = man_dist(min(coords, key=(lambda p: man_dist(p, pos))), pos)
    return [i for i, x in enumerate(coords) if man_dist(x, pos) == min_dist]


def a():
    coords = [tuple(map(int, coord.split(", "))) for coord in read_input(6)]
    max_x = max(coords, key=(lambda c: c[0]))[0]
    min_x = min(coords, key=(lambda c: c[0]))[0]
    max_y = max(coords, key=(lambda c: c[1]))[1]
    min_y = min(coords, key=(lambda c: c[1]))[1]

    grid = [["" for x in range(min_x - 10, max_x + 10)]
            for y in range(min_y - 10, max_y + 10)]

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            closest_points = get_closest_points(coords, (x, y))
            if len(closest_points) == 1:
                grid[x][y] = closest_points[0]
            else:
                grid[x][y] = ".."

    non_infinite = []

    for area in range(len(coords)):
        if area in grid[0] or \
           area in grid[-1] or \
           area in [row[0] for row in grid] or \
           area in [row[-1] for row in grid]:
            continue
        non_infinite.append(sum(row.count(area) for row in grid))

    return max(non_infinite)


def b():
    coords = [tuple(map(int, coord.split(", "))) for coord in read_input(6)]
    max_x = max(coords, key=(lambda c: c[0]))[0]
    min_x = min(coords, key=(lambda c: c[0]))[0]
    max_y = max(coords, key=(lambda c: c[1]))[1]
    min_y = min(coords, key=(lambda c: c[1]))[1]

    grid = [["" for x in range(min_x - 10, max_x + 10)]
            for y in range(min_y - 10, max_y + 10)]

    safe = []

    for x in range(min_x - 10, max_x + 10):
        for y in range(min_y - 10, max_y + 10):
            total_distance = sum(man_dist((x, y), pos) for pos in coords)
            if total_distance < 10000:
                safe.append((x, y))

    return len(safe)
