from core.fibonacci_helpers import create_sequence, locate


def play_fibonacci():
    command = input()
    sequence = []

    while command != "Stop":

        if command.startswith("Create"):
            n = int(command.split()[-1])
            sequence = create_sequence(n)
            print(*sequence)

        else:
            number = int(command.split()[-1])
            print(locate(number, sequence))

        command = input()
