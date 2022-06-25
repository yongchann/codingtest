from collections import defaultdict
import sys
input = sys.stdin.readline
d = defaultdict(list)
answer = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    d[y].append(x)    

for l in d.values():
    l.sort()
    for i in range(1, len(l)-1):
        answer += min(l[i] - l[i-1], l[i+1]-l[i])
    answer += (l[1] - l[0] + l[-1] - l[-2])
print(answer)