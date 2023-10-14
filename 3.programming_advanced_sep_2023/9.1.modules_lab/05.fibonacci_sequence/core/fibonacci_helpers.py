def create_sequence(n):
    seq = [0, 1]
    for _ in range(n - 2):
        current = seq[-1]
        prev = seq[-2]

        next_number = current + prev
        seq.append(next_number)
    return seq


def locate(number, seq):
    try:
        return f"The number - {number} is at index {seq.index(number)}"

    except ValueError:
        return f"The number {number} is not in the sequence"
