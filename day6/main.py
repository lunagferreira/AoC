import operator
import re
from functools import reduce


def read_grid(filename):
    """Read the input file and return a list of equal-length strings (the grid)."""
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    # Pad all lines with spaces so they all have the same length
    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len, " ") for line in lines]
    return padded


def find_problem_groups(grid):
    """Identify column ranges that correspond to individual problems."""
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Determine which columns are completely empty (all spaces)
    empty_col = []
    for col in range(num_cols):
        all_space = True
        for row in range(num_rows):
            if grid[row][col] != " ":
                all_space = False
                break
        empty_col.append(all_space)

    # Group non-empty columns into problems
    groups = []
    col = 0
    while col < num_cols:
        if empty_col[col]:
            col += 1
        else:
            start = col
            while col < num_cols and not empty_col[col]:
                col += 1
            end = col  # [start, end)
            groups.append((start, end))

    return groups


def parse_problem_part1(grid, col_start, col_end):
    """From a given column range extract list of numbers and operation."""
    num_rows = len(grid)
    operation_row = num_rows - 1

    # Find the operation in the last row in this column range
    operation_segment = grid[operation_row][col_start:col_end]
    operation = None
    if "+" in operation_segment:
        operation = "+"
    else:
        operation = "*"

    # Collect numbers from all rows except the last
    numbers = []
    for row in range(operation_row):
        segment = grid[row][col_start:col_end]
        # Regex to find any contiguous digits
        matches = re.findall(r"\d+", segment)
        for m in matches:
            numbers.append(int(m))

    return numbers, operation


def parse_problem_part2(grid, col_start, col_end):
    """From a given column range, extract list of numbers and operation,
    where each number is written vertically in a single column."""
    num_rows = len(grid)
    operation_row = num_rows - 1

    # Find the operation in the last row in this column range
    operation_segment = grid[operation_row][col_start:col_end]
    operation = None
    if "+" in operation_segment:
        operation = "+"
    else:
        operation = "*"

    # Collect numbers from all rows except the last
    numbers = []
    # For each column in this problem, read digits top-to-bottom
    for col in range(col_start, col_end):
        digits = []
        for row in range(operation_row):
            ch = grid[row][col]
            if ch.isdigit():
                digits.append(ch)

        if digits:
            # Each column corresponds to exactly one number
            num = int("".join(digits))
            numbers.append(num)

    return numbers, operation


def compute_problem_result(numbers, operation):
    """Compute the result of applying the operator operation to all numbers."""
    if operation == "+":
        return sum(numbers)
    else:
        return reduce(operator.mul, numbers, 1)


def main():
    grid = read_grid("input.txt")
    groups = find_problem_groups(grid)

    grand_total = 0

    for start, end in groups:
        numbers, operation = parse_problem_part2(grid, start, end)
        result = compute_problem_result(numbers, operation)
        grand_total += result

    print(grand_total)


if __name__ == "__main__":
    main()
