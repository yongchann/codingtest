import sys
input = sys.stdin.readline

n, m, b= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

now_max = max([max(i) for i in graph])
max_height = (b + sum([sum(i) for i in graph])) // (n * m)
min_time = 9876543210
level = -1
for height in range(max_height+1):
    sum_time = 0
    for y in range(n)s:
        for x in range(m):
            if graph[y][x] == height : continue
            elif graph[y][x] < height : min_time += height-graph[y][x]
            else : min_time += (graph[y][x]-height) * 2

    
    if sum_time < min_time:
        min_time = sum_time
        level = height