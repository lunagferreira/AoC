def is_invalid_id(n: int) -> bool:
    string = str(n)  # Convert number to string
    if len(string) % 2 != 0:  # Length must be even
        return False
    half = len(string) // 2  # Middle point
    return string[:half] == string[half:]  # Check if first half equals second half


def sum_invalid_ids(line: str) -> int:
    total = 0  # Sum of invalid IDs

    for part in line.split(","):  # Split on commas
        part = part.strip()  # Remove spaces
        if not part:  # Skip empty text
            continue

        start, end = map(int, part.split("-"))  # Get range bounds

        for n in range(start, end + 1):  # Loop through range
            if is_invalid_id(n):  # If invalid
                total += n  # Add to total

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:  # Open the input file
        input_line = f.read().strip()  # Read the whole line

    print(sum_invalid_ids(input_line))  # Print the result
