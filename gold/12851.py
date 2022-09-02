from collections import deque, defaultdict

n, k = map(int, input().split())
answer = defaultdict(int)
q = deque([(n, 0)])
visited = [0] * 100001
while q:
    now, cnt = q.popleft()
    if now == k:
        answer[cnt] += 1
        
    else:
        if 0<=now<=100000 and visited[now] <= 3:
            visited[now] += 1
            q.append((now+1, cnt+1))
            q.append((now-1, cnt+1))
            q.append((now*2, cnt+1))
        

print(list(answer.items())[0][0])
print(list(answer.items())[0][1])
