multi_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(multi_list)):
    multi_list[i] = multi_list[i][::-1]


print(multi_list)

# print([["*", "*", "*"] for i in range(1,4)])
print([[num , num + 1, num + 2 ] for num in range(1, 8, 3)])