from collections import deque
n, k, r = map(int, input().split())
road = [[[] for _ in range(n+1)] for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]
num_cow = []
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

#길 정보 저장 
for _ in range(r):
    y1, x1, y2, x2 = map(int, input().split())
    road[y1][x1].append((y2, x2))
    road[y2][x2].append((y1, x1))

#소 위치 저장
cows = [tuple(map(int, input().split())) for _ in range(k)]

def bfs(y, x, visited):
    q = deque([(y, x)])
    visited[y][x] = True
    cow = 1
    
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ny = _y + dy[i]
            nx = _x + dx[i]
            
            if 1<=ny<=n and 1<=nx<=n and not visited[ny][nx] and (ny, nx) not in road[_y][_x]:
                q.append((ny, nx))
                visited[ny][nx] = True
                if (ny,nx) in cows:
                    cow += 1
    return cow

#소 기준 탐색하면 리턴값 >= 1 보장됨         
for i, j in cows:
    if not visited[i][j]:
        num_cow.append(bfs(i, j, visited))
            
if len(num_cow) == 1:
    answer = num_cow[0]
    
else:
    for i in range(len(num_cow)-1):
        for j in range(i+1, len(num_cow)):
            answer += num_cow[i] * num_cow[j]

print(answer)