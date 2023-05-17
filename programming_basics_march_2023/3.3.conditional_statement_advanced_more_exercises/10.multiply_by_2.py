number = 0
double = 0

while number >= 0:
  number = float (input())
  double = number * 2
  if number >= 0:
    print(f'Result: {double:.2f}')
  else:
    print('Negative number!')
