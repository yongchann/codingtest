from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited[0][0][0], visited[0][0][1] = 1, 1
q = deque([(0, 0, 0)])

while q:
    y, x, wall_break = q.popleft()
    if y == n-1 and x == m-1:
        print(visited[y][x][wall_break])
        break
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<m:
            #벽 깬 적 없음 + 벽 만남 -> 부수거나 안가거나
            if not wall_break and graph[ny][nx] == '1':
                visited[ny][nx][1] = visited[y][x][0] + 1
                q.append((ny, nx, True))
                
            elif not visited[ny][nx][wall_break] and graph[ny][nx] == '0':
                visited[ny][nx][wall_break] = visited[y][x][wall_break] + 1
                q.append((ny, nx, wall_break))
else:
    print(-1)