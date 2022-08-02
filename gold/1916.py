from heapq import heappop, heappush
from math import dist
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [float("INF")] * (n+1)
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
a, b = map(int, input().split())
distance[a] = 0

q = []
heappush(q, (0, a))
while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue
    
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(q, (cost, i[0]))
    
print(distance[b])