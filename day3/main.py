def best_two_digits(line: str) -> tuple[int, int]:
    """
    Find the two digits in the line that form the largest two-digit number.
    """
    best_value = -1
    best_pair = (0, 0)
    n = len(line)

    for i in range(n - 1):
        if not line[i].isdigit():
            continue
        for j in range(i + 1, n):
            if not line[j].isdigit():
                continue

            digit1 = int(line[i])
            digit2 = int(line[j])
            value = 10 * digit1 + digit2  # two-digit number

            if value > best_value:
                best_value = value
                best_pair = (digit1, digit2)

    return best_pair


if __name__ == "__main__":
    digits = []

    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    # Loop through each line (each bank)
    for line in input_text.splitlines():
        line = line.strip()
        if not line:
            continue

        digit1, digit2 = best_two_digits(line)
        digits.append(digit1)
        digits.append(digit2)

    # Print the final two digits per row together
    for i in range(0, len(digits), 2):
        print(f"{digits[i]}{digits[i+1]}", end=" ")

    # Sum the numbers formed by the digit pairs
    total = 0
    for i in range(0, len(digits), 2):
        number = int(f"{digits[i]}{digits[i+1]}")
        total += number

    print(f"\nTotal: {total}")
