# put your python code here
first_hour = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hour = int(input())
second_minutes = int(input())
second_seconds = int(input())

first_total_seconds = first_hour * 3600 + first_minutes * 60 + first_seconds
second_total_seconds = second_hour * 3600 + second_minutes * 60 + second_seconds
difference = second_total_seconds - first_total_seconds
print(difference)
