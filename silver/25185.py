from itertools import combinations
n = int(input())
nlist = ['123','234','345','456','567','678','789']
answer = []
for _ in range(n):
    card = list(input().split())
    card.sort(key=lambda x : (x[0], x[1]))
    rest = False
    
    #case1
    for c in combinations(card,3):
        if c[0][0] + c[1][0] + c[2][0] in nlist and c[0][1] == c[1][1] and c[1][1] == c[2][1]:
            rest = True

    if not rest:
        if (card[0] == card[1] and card[1]==card[2]) or (card[1]==card[2] and card[2]==card[3]):
            rest = True
    
    if not rest:
        if card[0] == card[1] and card[2]==card[3]:
            rest = True
    
    if rest:
        answer.append(':)')
    else:
        answer.append(':(')

for i in answer:
    print(i)