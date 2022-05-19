from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)] 
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = deque()
def bfs(y, x, data):
    visited[y][x] = True
    queue.append((y, x))
    cnt = 1
    while queue:
        _y, _x = queue.popleft()
        for i in range(4):
            ny = _y + dy[i]
            nx = _x + dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and graph[ny][nx] == data:
                queue.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    
    return cnt
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and not visited[i][j]:
            data = graph[i][j]
            answer.append(bfs(i,j, data))
        
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])