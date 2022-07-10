import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

target_y, target_x = n-1, m-1
answer = 0

def dfs(y, x, value):
    global answer
    if y == target_y and x == target_x:
        answer += 1
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<m and graph[ny][nx] < value and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, graph[ny][nx])
            visited[ny][nx] = False

visited[0][0] = True
dfs(0, 0, graph[0][0])

print(answer)