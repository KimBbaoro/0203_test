poketmons = [["피카츄", "꼬북이", "파이리"],[200,150,100]]

new_pocket = ["치코리타", 175]

#체력으로 index를 찾고 각각 넣으면 될거 같네

length = len(poketmons[0])

def find_idx(poketmons, new_pocket, length):
    for i in range(length):
        if poketmons[1][i] <= new_pocket[1]:
            return i

    return length

def insert_pocket(poketmons,new_pocket,length):
    poketmons[0].append(None)
    poketmons[1].append(None)
    idx = find_idx(poketmons,new_pocket,length)
    length = len(poketmons[0])
    print("length : ", length)
    print("idx : ", idx)
    for i in range(length-1,idx,-1): #3,0
        poketmons[0][i] = poketmons[0][i-1]
        poketmons[0][i-1] = None
        poketmons[1][i] = poketmons[1][i-1]
        poketmons[1][i-1] = None
        print("poketmons : ", poketmons)

    poketmons[0][idx] = new_pocket[0]
    poketmons[1][idx] = new_pocket[1]

insert_pocket(poketmons,new_pocket,length)

print(poketmons)

