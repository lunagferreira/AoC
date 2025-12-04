def best_k_digits(line: str, k: int) -> list[int]:
    """
    Find the K digits in the line that form the largest K-digit number.
    """
    d = [digits for digits in line if digits.isdigit()]
    n = len(d)

    if k >= n:
        # If there are k or fewer digits, just take all
        return [int(digit) for digit in d]

    remove = n - k  # how many digits we are allowed to drop
    stack: list[str] = []

    for digits in d:
        while stack and remove > 0 and stack[-1] < digits:
            stack.pop()
            remove -= 1
        stack.append(digits)

    # If we still have removals left, drop from the end
    if remove > 0:
        stack = stack[:-remove]

    # Take exactly k digits (in case stack is longer)
    stack = stack[:k]

    return (int(digit) for digit in stack)


if __name__ == "__main__":
    d = []

    with open("input.txt", "r") as f:
        input_text = f.read().strip()

    K = 12  # number of batteries to turn on

    # Loop through each line (each bank)
    for line in input_text.splitlines():
        line = line.strip()
        if not line:
            continue

        chosen = best_k_digits(line, K)  # list of 12 digits
        d.extend(chosen)

    # Print the final K digits per row together
    for i in range(0, len(d), K):
        num_str = "".join(str(digit) for digit in d[i : i + K])
        print(num_str, end=" ")

    # Sum the numbers formed by the digit pairs
    total = 0
    for i in range(0, len(d), K):
        num_str = "".join(str(digit) for digit in d[i : i + K])
        total += int(num_str)

    print(f"\nTotal: {total}")
