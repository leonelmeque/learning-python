nums = (1, 2, 3)
print(1 in nums)
print(nums[2]) # accessing value at index
print(nums.count) # counting number of items
print(nums.index(1)) # index value

# tuple inside a tuple
tuple_dub = (1,2,3,(4,5))
print(tuple_dub)

cities = ['New York', 'New York', 'Los Angeles', 'San Francisco', 'San Francisco', 'San Francisco']
s = set(cities)
print(set(cities))

print(2 in s)

for city in s:
    print(city)

s.add('Chicago')
print(s)

s.discard(1)
print(s)

# Suppose I teach two classes:
math_student = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

print(math_student | biology_students)
print(math_student & biology_students)


