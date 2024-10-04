# Loop through 1 to 20

for num in range(1,20):

    if num == 4 or num == 13:
        print(f"{num} is Unlucky")
        continue

    if num % 2 == 0:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")