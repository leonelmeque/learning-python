def greet_people():
    print('Hello')


greet_people()

nums = [1, 2, 3, 4]


def print_square_of_7():
    return [x ** 7 for x in nums]


print(f"Square of seven " + ' '.join(map(str, print_square_of_7())))


def greet_by_name(name):
    print(f'Hello {name}')


greet_by_name("Leo")
