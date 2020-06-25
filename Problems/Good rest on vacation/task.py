# put your python code here
num_day = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

total_cost = (food_cost * num_day) + (2 * flight_cost)
total_cost += (hotel_cost * (num_day - 1))

print(total_cost)
