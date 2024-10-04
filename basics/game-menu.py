print("Fallout 4")

op = input("Do you want to play Fallout 4? (yes/no) \n")

while op != "yes":
    print("You are missing out!")
    op = input("Do you want to play Fallout 4? (yes/no) \n")

print("Welcome to Fallout 4!")

op = input("Enter your name: \n")
while len(op) == 0:
    print("You must enter a name to continue!")
    op = input("Enter your name: \n")

name = op

print(f"Welcome {name} to Fallout 4!")