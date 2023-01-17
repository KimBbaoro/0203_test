start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("flop", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for start_1 in start1:
    print(start_1.capitalize() + '!', end=' ')
print()
print(start2 + ' ', end = ' ')
print(rhymes[0][1])
