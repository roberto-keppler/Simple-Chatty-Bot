# put your python code here
duration = int(input())
daily_food_cost = int(input())
one_way_flight = int(input())
nightly_hotel_cost = int(input())

total_cost = daily_food_cost * duration + 2 * one_way_flight + (duration - 1) * nightly_hotel_cost
print(total_cost)
