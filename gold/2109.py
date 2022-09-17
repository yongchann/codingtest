from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: x[1])

q = []
    
for price, deadline in info:
    heappush(q, price)
    if deadline < len(q):
        heappop(q)

print(sum(q))
    