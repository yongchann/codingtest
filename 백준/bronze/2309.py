from itertools import combinations
l = [int(input()) for _ in range(9)]
answer = []
l.sort()
hap = sum(l)
for comb in combinations(l,2):
    if sum(comb) == hap - 100:
        answer = comb
        break
    
for i in l:
    if i not in answer:
        print(i)