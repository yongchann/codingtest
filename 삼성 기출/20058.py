from collections import deque

n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**n)]
l = list(map(int, input().split()))
visited = [[False] * 2**n for _ in range(2**n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    ret = 1
    q = deque([(y, x)])
    visited[y][x] = True
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ny = _y + dy[i]; nx = _x + dx[i]
            if 0<=ny<2**n and 0<=nx<2**n and not visited[ny][nx] and graph[ny][nx]:
                ret += 1
                visited[ny][nx] = True
                q.append((ny, nx))
    return ret

def fire_storm(level):
    for i in range(0, 2**n, 2**level):
        for j in range(0, 2**n, 2**level):
            rotate(i, j, level)
    temp = []
    for i in range(2**n):
        for j in range(2**n):
            if graph[i][j] and check_ice(i, j) < 3:
                temp.append((i, j))
    while temp:
        y, x = temp.pop()
        graph[y][x] -= 1
        
def rotate(y, x, level):
    temp = [graph[y+k][x:x+2**level] for k in range(2**level)][:]
    temp = list(zip(*temp[::-1]))
    for i in range(2**level):
        for j in range(2**level):
            graph[y+i][x+j] = temp[i][j]
    
def check_ice(y, x):
    ret = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<2**n and 0<=nx<2**n and graph[ny][nx]:
            ret += 1
    return ret
        
for level in l:
    fire_storm(level)
left_ices = sum(sum(i) for i in graph)
max_ice = 0
for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j] and graph[i][j]:
            max_ice = max(max_ice, bfs(i, j))

print(left_ices, max_ice)
