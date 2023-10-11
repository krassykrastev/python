# Create a module that does basic calculations.
#
# Input1:
# 2.5 * 2
#
# Output1:
# 5.0
#
# Input2:
# 6.66 ^ 2
#
# Output2:
# 44.35

from core.executor import execute_string

expression = input()

print(f"{execute_string(expression):.2f}")
