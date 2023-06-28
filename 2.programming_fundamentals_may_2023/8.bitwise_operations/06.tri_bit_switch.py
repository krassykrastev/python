# Write a program that inverts the 3 bits from position p to the left with their XOR opposites (e.g., 111 -> 000, 101 -> 010) in a 32-bit number.
# Print the resulting integer on the console.

number = int(input())
position = int(input())

mask = 7 << position
inverted_bits = mask ^ number

print(inverted_bits)