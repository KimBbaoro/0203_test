def get_odds():
    return [odd_num for odd_num in range(1,10,2)]

for i in range(len(get_odds())):
    if i == 2:
        print(get_odds()[i])