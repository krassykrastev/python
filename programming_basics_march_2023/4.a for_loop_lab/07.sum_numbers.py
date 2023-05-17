count = int(input())
value = 0

for _ in range(count): #когато една променлива не се използва, се слага _
    num = int(input())
    value += num

print(value)
