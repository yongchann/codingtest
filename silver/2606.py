from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    answer = 0
    queue = deque([v])
    visited[v] = True
    
    while queue:
        a = queue.popleft()
        for u in graph[a]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                answer += 1
    return answer

print(bfs(1))