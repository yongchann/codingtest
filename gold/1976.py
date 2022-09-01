n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if i == j : graph[i][i] = 1
        if graph[i][j] == 0:
            graph[i][j] = float("INF")
        
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

l = list(zip(route, route[1:]))
answer = 'YES'
for move in l:
    if graph[move[0]-1][move[1]-1] == float("INF"):
        answer = 'NO'
        break
print(answer)