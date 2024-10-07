name = "colt"
print([char.upper() for char in name])

print([num*10 for num in range(1,6)])

numbers = [1,2,3,4,5]

evens = [num for num in numbers if num % 2 == 0]
print(f"even numbers {evens}")

odds = [num for num in numbers if num % 2 != 0]
print(f"odd numbers {odds}")

with_vowels = "This is so much fun!"

print(''.join(char for char in with_vowels if char not in "aeiou"))
print(''.join(with_vowels.split(' '))[::-1])