from itertools import combinations
n, s = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
for i in range(1, len(l) + 1):
    for j in combinations(l,i):
        if sum(list(j)) == s:
            cnt += 1

print(cnt)
