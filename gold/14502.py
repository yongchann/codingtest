from copy import deepcopy
from collections import deque
from itertools import combinations

m,n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]
    
#벽 세우기 유망한 위치 set에 저장 -> m,n 작아서 굳이 안해도 됨.. -> 입력 크기 확인 후 brute force 가능한지 체크 
walls = []
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            walls.append((y,x))
            
max_safe = 0
#벽 고른 경우마다 BFS로 채우고 0 탐색 
for wall in combinations(walls, 3):
    temp = deepcopy(graph)
    virus = deque()
    for i in range(m):
        for j in range(n):
            if temp[i][j] == 2:
                virus.append([i,j])
    for i in range(3):
        y, x = wall[i][0], wall[i][1]
        temp[y][x] = 1
        
    #BFS
    while virus:
        _y, _x = virus.popleft()
        for i in range(4):
            ny = _y + dy[i]
            nx = _x + dx[i]
            if 0<=ny<m and 0<=nx<n and temp[ny][nx] == 0:
                virus.append((ny,nx))
                temp[ny][nx] = 2
                
    #케이스마다 안전영역 크기 계산            
    cnt = 0
    for i in range(m):
        cnt += temp[i].count(0)
    max_safe = max(max_safe, cnt)
print(max_safe)