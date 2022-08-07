from itertools import combinations, permutations
n, m = map(int, input().split())
l = list(map(int, input().split()))
s = set()

for i in combinations(l, m):
    temp = permutations(i)
    for j in temp:
        s.add(j)

for i in sorted(list(s)):
    print(*i)