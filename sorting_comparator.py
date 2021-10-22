import sys
from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # def __repr__(self):
        
    def comparator(a, b):
        swap = 1
        no_swap = -1
        if a.score < b.score:
            return swap
        elif a.score > b.score:
            return no_swap
        else:
            if a.name > b.name:
                return swap
            elif a.name < b.name:
                return no_swap
        return 0

infile = open(sys.argv[1])
n = int(infile.readline().strip())
data = []
for i in range(n):
    name, score = infile.readline().strip().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)