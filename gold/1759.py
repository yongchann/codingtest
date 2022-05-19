from itertools import combinations
l, c = map(int, input().split())
chars = sorted(input().split())
consonant = 'aeiou'

for set in combinations(chars, l):
    nc, nv = 0, 0
    
    for i in set:
        if i in consonant:
            nc += 1
        else :
            nv += 1
    
    if nc >= 1 and nv >= 2:
        print(''.join(set))