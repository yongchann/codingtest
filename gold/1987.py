import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [False] * 100
answer = 0


def dfs(y, x, visited, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m:
            if visited[ord(graph[ny][nx])] == False:
                visited[ord(graph[ny][nx])] = True
                dfs(ny, nx, visited, cnt + 1)
                visited[ord(graph[ny][nx])] = False
        
cnt = 1
visited[ord(graph[0][0])] = True
dfs(0, 0, visited, cnt)

print(answer)

