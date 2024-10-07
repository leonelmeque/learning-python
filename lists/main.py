numbers = [1,2,3,4,5]

# list of country names
countries = ['India', 'USA', 'UK', 'Canada']

print(f"==== Appending a new country to the list")
countries.append("Mozambique")
countries.append("South Africa")
countries.append("Canada")
countries.extend(["France", "Namibia", "Seychelles", "Cape Verde"])

print(countries)

print(f"==== Adding a new country to the list in the third position")
countries.insert(2, "Brazil")
print(countries)

print("===== Removing a country from the list, (the last)")
countries.pop()
print(countries)


print("===== Removing a country at the third position")
countries.pop(2)
print(countries)

print(f"====== Counting the number of times Canada shows up in the list")
print(countries)
print(countries.count("Canada"))

print(f"====== Removing Canada from the list")
countries.remove("Canada")
print(countries)

print("====== Finding the index of France")
print(countries.index("France"))

print("====== Reversing the list")
countries.reverse()
print(countries)

print("====== Sort the data")
countries.sort()
print(countries)

print(f"===== Join list with '->'")
introduction = " -> "
print(introduction.join(countries) + ' .')

print(f"===== Copying the last 2 items of a list to another var")
copy_of_countries = countries[-2:]
print(countries)
print(copy_of_countries)

print(f"===== Get elements from the 3 item until the 5 item")
copy_of_countries = countries[3:5]
print(countries)
print(copy_of_countries)


print(f"===== Replacing countries with numbers")
countries[3:5] = [1,2,3]
print(countries)

print(f"==== Reverse the letters of the first country")
print(countries[0][::-1])

print("====== Cleaning the whole list")
countries.clear()
print(countries)
