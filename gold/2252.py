from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
q, answer = deque(), []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    visited[b] += 1

for i in range(1, n+1):
    if not visited[i]:
        q.append(i)
        
# q = [3, 4]

while q:
    v = q.popleft()
    answer.append(v)
    
    for u in graph[v]:
        if visited[u]:
            visited[u] -= 1
        
        if not visited[u]:
            q.append(u)
            

print(answer)
        