halls_number = int(input())
capacity_of_hall = int(input())
number_of_viewers = int(input())
total_capacity = halls_number * capacity_of_hall
can_accommodate = total_capacity >= number_of_viewers
print(can_accommodate)
