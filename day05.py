test = [num for num in range(10)]
print(type(i for i in range(10)))

def odd_nums():
    return (odd_num for odd_num in range(1,10,2))

# for i in range(len(list(odd_nums()))):
#     if i == 2:
#         print(list(odd_nums())[2])

for i,j in enumerate(odd_nums()):
    if i ==2:
        print(j)


