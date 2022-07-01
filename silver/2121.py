from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
d = defaultdict(int)
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    d[(x,y)] += 1

l = list(d.keys())[:]
for x, y in l:
    if d[(x+a, y)] and d[(x, y+b)] and d[(x+a, y+b)]:
        answer += 1
    
print(answer)
