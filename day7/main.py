def read_grid(path: str):
    with open(path, "r", encoding="utf-8") as f:
        grid = [line.rstrip("\n") for line in f]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    start_row = start_col = None
    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            start_row, start_col = r, c
            break

    return grid, rows, cols, start_row, start_col


def count_splits(grid, rows, cols, start_row, start_col):
    # Set of columns where there is at least one beam on the current row
    beams = {start_col}
    splits = 0

    # Start just below S
    for r in range(start_row + 1, rows):
        if not beams:
            break  # no beams left, nothing more can happen

        new_beams = set()

        for c in beams:
            # Beam is currently at (r, c)
            cell = grid[r][c]

            if cell == "^":
                # Beam hits splitter: it is split
                splits += 1

                # Create new beams to the left and right (if in bounds)
                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < cols:
                    new_beams.add(c + 1)
            else:
                # Empty (.) or any non-splitter: beam continues straight down
                new_beams.add(c)

        beams = new_beams

    return splits


def main():
    grid, rows, cols, sr, sc = read_grid("input.txt")
    result = count_splits(grid, rows, cols, sr, sc)
    print(result)


if __name__ == "__main__":
    main()
