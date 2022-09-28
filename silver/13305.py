from collections import deque

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))[:-1]

answer = 0
min_cost = costs[0]
for i in range(n-1):
    if costs[i] < min_cost:
        min_cost = costs[i]
    answer += min_cost * distances[i]

print(answer)    