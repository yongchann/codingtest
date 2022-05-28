import heapq
import sys
input = sys.stdin.readline
n = int(input())
l = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if l:
            print(heapq.heappop(l))
        else:
            print(0)
        
    else:
        heapq.heappush(l, x)
    
    