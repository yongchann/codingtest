from collections import deque
n, m = map(int, input().split())
snake_or_ladder = [0] * 101
visited = [0] * 1000

for _ in range(n+m):
    x, y = map(int, input().split())
    snake_or_ladder[x] = y

q = deque([(1, 0)])
visited[1] = True
while q:
    v = q.popleft()
    if v[0] == 100:
        print(v[1])
        break
    
    for i in range(1, 7):
        if visited[v[0] + i] or v[0] + i > 100:
            continue
        
        if snake_or_ladder[v[0] + i]:
            q.append((snake_or_ladder[v[0] + i], v[1] + 1))
            visited[snake_or_ladder[v[0] + i]] = True
         
        else:
            q.append((v[0] + i, v[1] + 1))
            visited[v[0] + i] = True
            
    