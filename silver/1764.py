from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = defaultdict(int)

for _ in range(n):
    d[input().strip()] += 1
    
for _ in range(m):
    d[input().strip()] += 1
    
l = sorted([i[0] for i in d.items() if i[1] == 2])
print(len(l))
for i in l:
    print(i)