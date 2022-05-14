# put your code here
number = int(input())
sum_of_numbers = 0
count = 0

while number != 55:
    sum_of_numbers += number
    count += 1
    number = int(input())

print(count)
print(sum_of_numbers)
print(round(sum_of_numbers / count))
