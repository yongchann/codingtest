import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    if visited[y][x] == True:
        return dp[y][x]
    
    if y == n-1 and x == m-1:
        return 1
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if 0<=ny<n and 0<=nx<m and graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(ny, nx)
    
    visited[y][x] = True
    
    return dp[y][x]

a = dfs(0, 0)
print(a)
    