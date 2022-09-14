from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, visited):
    q = deque([(y, x)])
    visited[y][x] = True
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ny, nx = _y + dy[i], _x + dx[i]
            if 1<=ny<n-1 and 1<=nx<m-1 and not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
    
def count():
    ret = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j, visited)
                ret += 1
    return ret

def melting():
    temp = [[0] * m for i in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j]:
                cnt = 0 
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if graph[ny][nx] == 0:
                        cnt += 1
                temp[i][j] = max(0, graph[i][j] - cnt)
    for i in range(n):
        graph[i] = temp[i]

while True:
    if count() >= 2 or not sum(sum(graph[i]) for i in range(n)):
        break
    melting()
    answer += 1
    
print(answer if sum(sum(graph[i]) for i in range(n)) else 0)