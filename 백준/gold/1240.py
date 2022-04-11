from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def getDist(x, y):
    q = deque([(x, 0)])
    visited = [False] * (n+1)
    visited[x] = True
    
    while q:
        v, d = q.popleft()
        if v == y:
            return d
        for w, dist in graph[v]:
            if not visited[w]:
                visited[w] = True
                q.append((w, d+dist))

for _ in range(n-1):
    i, j, dist = map(int, input().split())
    
    graph[i].append((j, dist))
    graph[j].append((i, dist))
    
for _ in range(m):
    x, y = map(int, input().split())
    print(getDist(x, y))
    