from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque([])
d = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1]]

#익은 토마토 q에 추가
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])

#q가 빌 때까지 bfs 진행
while q:
    t = q.popleft()
    
    for i in range(6):
        nz = t[0] + d[i][0] 
        ny = t[1] + d[i][1]
        nx = t[2] + d[i][2]
        if 0<=nz<h and 0<=ny<n and 0<=nx<m and tomato[nz][ny][nx] == 0:
            q.append([nz, ny, nx])   
            tomato[nz][ny][nx] = tomato[t[0]][t[1]][t[2]] + 1

#상자 돌면서 answer 갱신, 익지 않은 토마토 발견시 -1 출력 후 종료
answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
                
        answer = max(answer, max(tomato[i][j]))
            
print(answer-1)