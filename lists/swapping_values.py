positions = ["first", "second", "third"]
print(f"Before the swap: {" ".join(positions)}")

positions[0], positions[1] = positions[1], positions[0]
print(f"After the swap: {" ".join(positions)}")