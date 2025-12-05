def count_accessible(grid):
    rows = len(grid)
    cols = len(grid[0])

    # 8 neighbours around each cell
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue  # skip anything that's not a roll

            neighbours = 0
            # check all surrounding positions
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # make sure we stay inside the grid
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        neighbours += 1

            # if fewer than 4 neighbours, it's accessible
            if neighbours < 4:
                total += 1

    return total


def total_removed(grid):
    rows = len(grid)
    cols = len(grid[0])

    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # turn strings into lists so we can modify the grid
    g = [list(row) for row in grid]

    removed_sum = 0

    while True:
        to_remove = []

        # find all rolls that are currently accessible
        for r in range(rows):
            for c in range(cols):
                if g[r][c] != "@":
                    continue

                neighbours = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if g[nr][nc] == "@":
                            neighbours += 1

                if neighbours < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break  # no more rolls can be removed

        # remove all rolls found in this round
        for r, c in to_remove:
            g[r][c] = "."  # mark as empty

        removed_sum += len(to_remove)

    return removed_sum


if __name__ == "__main__":
    grid = []
    with open("ex.txt") as f:
        for line in f:
            line = line.strip()
            if line:  # just ignore empty lines
                grid.append(line)

    # part 1: rolls accessible in the original layout
    result1 = count_accessible(grid)
    print(result1)

    # part 2: total rolls you can remove by repeating the process
    result2 = total_removed(grid)
    print(result2)
