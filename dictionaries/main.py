cat = {
    "name": "blue",
    "age": 3.8,
    "isCute": True
}

cat2 = dict(name="Kity")

print(cat)
print(cat2)
print(cat2['name'])
print(cat2.get('na', 'not_available'))

# accessing value only
for value in cat.values():
    print(value)

# accessing keys only
for key in cat.keys():
    print(key)

# accessing keys and values
for key, value in cat.items():
    print(f"Key is {key} and value is {value}")

# checking if key exists
print(f"Question: Does phone exists in Cat?\nAnswer: {'yes' if "phone" in cat else 'no'}")

# copying a dictionary
clone = cat.copy()
print(cat2)

# fromkeys to init empty values
new_user = {}.fromkeys(['name', 'age', 'score'], 'Unknown')
print(new_user)

keys_of_letter = {}.fromkeys("phone", 0)
print(keys_of_letter)

# removing keys of a dictionary, always needs an argument
keys_of_letter.pop('p')
print(keys_of_letter)

# removing keys with popItem, it will remove a random key
keys_of_letter.popitem()
print(keys_of_letter)

# update, will update
basic_info = dict(city="",height=None, weight=None)
person = dict(city="Barcelona", age=24)
person.update(basic_info)
print(person)

# clearing a dictionary
cat.clear()
print(cat)


