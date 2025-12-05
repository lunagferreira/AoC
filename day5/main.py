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


def count_fresh_ingredients(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    fresh_count = 0

    for ingredient_id in ids:
        is_fresh = any(start <= ingredient_id <= end for start, end in ranges)
        if is_fresh:
            fresh_count += 1

    return fresh_count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    ranges, ids = parse_ranges_and_ids(lines)
    fresh_count = count_fresh_ingredients(ranges, ids)
    print(fresh_count)
