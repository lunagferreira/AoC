def parse_ranges_and_ids(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ids = []
    parsing_ranges = True

    for line in lines:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Take a list of ranges and merge any that overlap or touch each other.
    """

    # If the list is empty, nothing to merge
    if not ranges:
        return []

    # Sort ranges so they are in order by their start value
    ranges = sorted(ranges, key=lambda r: r[0])

    merged_ranges = []

    # First range is current working range
    current_start, current_end = ranges[0]

    # Look at every other range one by one
    for start, end in ranges[1:]:

        # Next range overlaps or touches the current range
        if start <= current_end + 1:
            # Extend the current range to include the new one
            if end > current_end:
                current_end = end

        else:
            # Next range does not overlap or touch: save and next
            merged_ranges.append((current_start, current_end))
            current_start = start
            current_end = end

    # Save last range
    merged_ranges.append((current_start, current_end))

    return merged_ranges


def count_fresh_ingredients(ranges: list[tuple[int, int]]) -> int:
    merged = merge_ranges(ranges)
    # Sum length of each merged interval (inclusive)
    return sum(end - start + 1 for start, end in merged)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    ranges, _ = parse_ranges_and_ids(lines)
    fresh_count = count_fresh_ingredients(ranges)
    print(fresh_count)
