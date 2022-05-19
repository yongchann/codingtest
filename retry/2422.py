from itertools import combinations

n, m = map(int, input().split())

l = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    l[a].append(b)

print(l)