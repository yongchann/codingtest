from itertools import permutations
from collections import deque

n = int(input())
hp = list(map(int, input().split())) + [0] * (3-n)
hp.sort()
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]

damages = list(permutations([1,3,9]))
q = deque([(hp, 0)])

while q:
    now, cnt = q.popleft()
    if all([i == 0 for i in now]):
        print(cnt)
        break
        
    for damage in damages:
        v = [i-j if i-j > 0 else 0 for i, j in zip(now, damage)]
        v.sort()
        
        if not dp[v[0]][v[1]][v[2]]:
            dp[v[0]][v[1]][v[2]] = cnt + 1
            q.append([v, cnt+1])
