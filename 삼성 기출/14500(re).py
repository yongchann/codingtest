import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]


def dfs(y, x, d, total):
    global answer
    
    if d == 3:
        answer = max(answer, total)
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            
            if d == 1:
                visited[ny][nx] = True
                dfs(y, x, d+1, total+graph[ny][nx])
                visited[ny][nx] = False
                
            visited[ny][nx] = True
            dfs(ny, nx, d+1, total+graph[ny][nx])
            visited[ny][nx] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

print(answer)