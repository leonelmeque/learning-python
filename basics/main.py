# variables
greetings = "Hello, World!"
first_num = 1
second_num = 2

sum_of = first_num + second_num

print(greetings)
print(sum_of)
print(type(sum_of))

# Python support boolean, string, integer, float, list, tuple, dictionary, set, None

temperature_list = [12, 23, -12, -5]

print(temperature_list[1])

# get the last element from list
print(temperature_list[-1])

temperature_list.append(10)
print(temperature_list[-1])

user_name = input("Please write your name: \n")
print("Greetings %s" % user_name)

user_age = input("Please write your age: \n")
print(f"You are {user_age} years old")

# convert string to integer
print(type(int(user_age)))


first_num, second_num = input("Add two numbers to be sum: \n").split()
print(f"The result will be {int(first_num) + int(second_num)}")