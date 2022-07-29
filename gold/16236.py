from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
fish = dict()
shark_y, shark_x, shark_size, kill = -1, -1, 2, 0

def get_distance(y, x):
    global shark_y, shark_x
    visited = [[False] * n for _ in range(n)]
    visited[shark_y][shark_x] = True
    q = deque([[shark_y, shark_x, 0]])
    while q:
        sy, sx, d = q.popleft()
        if sy == y and sx == x:
            return d
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if space[ny][nx] <= shark_size:
                    q.append([ny, nx, d+1])
                    visited[ny][nx] = True


for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_y, shark_x = i, j
            space[i][j] = 0
        elif space[i][j] != 0:
            fish[(i, j)] = space[i][j]

while True:
    target = []
    for y, x in fish:
        if fish[(y, x)] < shark_size:
            target.append((y, x))
    
    if not target: 
        break
    
    if len(target) == 1:
        target_y, target_x = target[0]
        distance = get_distance(target_y, target_x)
        
    else:
        #거리 제일 가까운 애 찾기
        distance = float("INF")
        for i, j in target:
            temp = get_distance(i, j)
            if temp < distance:
                distance = temp
                target_y, target_x = i, j
            elif temp == distance:
                target_y, target_x = sorted([(target_y, target_x), (i, j)])[0]
                
    shark_y, shark_x = target_y, target_x
    fish.pop((target_y, target_x))
    
    answer += distance
    kill += 1
    if shark_size == kill:
        shark_size += 1
        kill = 0

print(answer)
