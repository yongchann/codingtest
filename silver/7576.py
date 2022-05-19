from collections import deque
m, n = map(int, input().split())
tomato = []
queue = deque(list())
for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs():
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and tomato[ny][nx] == 0:
                queue.append([ny,nx])
                tomato[ny][nx] = tomato[y][x] + 1


bfs()
answer = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(tomato[i]))
print(answer - 1)
#BFS 실행 -> 0있으면 -1 리턴 