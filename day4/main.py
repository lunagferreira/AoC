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


if __name__ == "__main__":
    grid = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:  # just ignore empty lines
                grid.append(line)

    result = count_accessible(grid)
    print(result)
