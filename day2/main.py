def is_invalid_id(n: int) -> bool:
    string = str(n)  # Convert number to string
    Lenght = len(string)  # Get length of string

    for block_lenght in range(
        1, Lenght // 2 + 1
    ):  # Loop through possible block lengths
        if Lenght % block_lenght != 0:  # If not divisible, skip
            continue

        repeats = Lenght // block_lenght  # Calculate number of repeats
        if repeats < 2:  # Need at least two repeats
            continue

        block = string[:block_lenght]  # Get the block to compare
        if block * repeats == string:  # Check if the string is made of repeated blocks
            return True  # It's an invalid ID

    return False  # It's a valid ID


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
