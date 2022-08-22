from collections import Counter
from itertools import combinations
target = input()
n = int(input())
infos = [input().split() for _ in range(n)]
answer = float("INF")
found = False
for i in range(1, n+1):
    for info in combinations(infos, i):
        price, temp = 0, ""
        for data in info:
            price += int(data[0])
            temp += data[1]
            
        if (Counter(temp) & Counter(target)) == Counter(target):
            answer = min(answer, price)
            found = True
            
print(answer if found else -1)