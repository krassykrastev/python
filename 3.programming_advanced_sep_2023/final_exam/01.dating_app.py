from collections import deque

males = [int(_) for _ in input().split(" ")]
females = deque([int(_) for _ in input().split(" ")])
matches_count = 0


def print_result(males, females):
    print(f"Matches: {matches_count}")
    if not males:
        print("Males left: none")
    else:
        print(f"Males left: {', '.join([str(m) for m in males[::-1]])}")
    if not females:
        print("Females left: none")
    else:
        print(f"Females left: {', '.join([str(f) for f in females])}")


while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    elif males[-1] <= 0:
        males.pop()
        continue

    elif females and females[0] % 25 == 0:
        females.popleft()
        females.popleft()
    elif males and males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    elif females[0] == males[-1]:
        females.popleft()
        males.pop()
        matches_count += 1
    else:
        females.popleft()
        males[-1] -= 2

print_result(males, females)