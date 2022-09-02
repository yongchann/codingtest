from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
shark_y, shark_x, shark_size, kill = -1, -1, 2, 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def get_food(shark_y, shark_x):
    global shark_size
    visited = [[False] * n for _ in range(n)]
    visited[shark_y][shark_x] = True
    q = deque([[0, shark_y, shark_x]])
    ret = []
    
    while q:
        d, y, x = q.popleft()
        if 0 < space[y][x] < shark_size and d > 0:
            ret.append([d, y, x])
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if space[ny][nx] <= shark_size:
                    q.append([d + 1, ny, nx])
                    visited[ny][nx] = True
    return ret

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_y, shark_x = i, j
            space[i][j] = 0
    
while True:
    can_eat = sorted(get_food(shark_y, shark_x))
    
    if not can_eat:
        break
    
    else:
        answer += can_eat[0][0]
        shark_y, shark_x = can_eat[0][1], can_eat[0][2]
        space[shark_y][shark_x] = 0
        
        kill += 1
        if kill == shark_size:
            shark_size += 1
            kill = 0

print(answer)