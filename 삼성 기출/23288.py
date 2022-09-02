from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
room_score = [[0] * m for _ in range(n)]

dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
bottom, direction = 6, 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0
now_y, now_x = 0, 0

def get_score(i ,j):
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    q = deque([(i, j)])
    cnt = 0
    
    while q:
        y, x = q.popleft()
        if graph[y][x] == graph[i][j]: cnt += 1
        for k in range(4):
            ny = y + dy[k]; nx = x + dx[k]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx] == graph[i][j]:
                visited[ny][nx] = True
                q.append((ny, nx))
    return cnt * graph[i][j]

def movable(y, x, d):
    ny = y + dy[d]
    nx = x + dx[d]
    if 0<=ny<n and 0<=nx<m:
        return True
    return False

def move(d):
    if d == 0:
        dice[3][1], dice[0][1], dice[1][1], dice[2][1] = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
    elif d == 2:
        dice[1][1], dice[2][1], dice[3][1], dice[0][1] = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
    elif d == 1:
        dice[1][1], dice[1][2], dice[3][1], dice[1][0] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
    else:
        dice[3][1], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
    
    return dice[3][1]
          
for i in range(k):
    if not movable(now_y, now_x, direction):
        direction = (direction + 2) % 4
    now_y += dy[direction]
    now_x += dx[direction]
    
    answer += get_score(now_y, now_x)
    bottom = move(direction)
    
    if bottom > graph[now_y][now_x]:
        direction = (direction + 1) % 4
    elif bottom < graph[now_y][now_x]:
        direction = (direction - 1) % 4

print(answer)
