import heapq
import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
heapq.heapify(l)
# for i in range(n):
    # heapq.heappush(l, int(input()))

res = 0
while len(l) > 1:
    a, b = heapq.heappop(l), heapq.heappop(l)
    heapq.heappush(l, a+b)
    res += a+b
    
print(res)
