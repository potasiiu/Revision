"""This code list the numbers from 20-25 and then adds their sum"""

numbers = list(range(20,26))
for number in numbers:
    print(number)
print(f"The sum of all these numbers is {sum(numbers)}")
