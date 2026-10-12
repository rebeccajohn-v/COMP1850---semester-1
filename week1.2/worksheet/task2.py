# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys

numbers = read_numbers()

if numbers == []:
    sys.exit("Error: no numbers provided")

mini = min(numbers)
maxi = max(numbers)
mean = sum(numbers) / len(numbers)
numbers.sort()

if len(numbers) % 2 == 0:
    median = (numbers[(len(numbers)//2) - 1] + numbers[len(numbers)//2]) / 2

else:
    median = numbers[len(numbers)//2]

print(f"Minimum = {mini}")
print(f"Maximum = {maxi}")
print(f"Mean = {mean}")
print(f"Median = {median}")

