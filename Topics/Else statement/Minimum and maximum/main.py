first_number = int(input())
second_number = int(input())
maximum = first_number
minimum = second_number
if maximum < second_number:
    minimum = first_number
    maximum = second_number
print(maximum)
print(minimum)
