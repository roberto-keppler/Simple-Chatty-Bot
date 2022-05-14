# put your python code here
first_class = int(input())
second_class = int(input())
third_class = int(input())
first_class_chairs = first_class // 2 + first_class % 2
second_class_chairs = second_class // 2 + second_class % 2
third_class_chairs = third_class // 2 + third_class % 2
total_chairs = first_class_chairs + second_class_chairs + third_class_chairs
print(total_chairs)
