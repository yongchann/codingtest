from itertools import combinations_with_replacement
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in combinations_with_replacement(l, m):
    print(*i)