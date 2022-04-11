from collections import deque
f, s, g, u, d = map(int, input().split())
#f층 짜리 건물, 현재 s층에서 g층에 가야함
#u 만큼 위로 가는 버튼, d 만큼 아래로 가는 버튼 두개만 존재
#버튼 수의 최솟값 구하기, 안되면 "use the stairs" 

visited = [0] * (f + 1)
visited[s] = 1
queue = deque([s])

while queue:
    now = queue.popleft()
    if now == g:
        print(visited[now] - 1)
        exit(0)        
        
        
    up, down = now + u, now - d
    if up <= f and not visited[up]:
        queue.append(up)
        visited[up] = visited[now] + 1
    if down >= 1 and not visited[down]:
        queue.append(down)
        visited[down] = visited[now] + 1
    

print('use the stairs')