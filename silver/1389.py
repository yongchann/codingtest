from collections import deque

#i번째 유저가 j번째 유저까지 가는 최소 거리 bfs
def bfs(i, j):
    visited = [False] * (n+1)
    visited[i] = True
    
    q = deque([[i, 0]])
    while q:
        v = q.popleft()
        if v[0] == j:
            return v[1]
        for u in graph[v[0]]:
            visited[u] = True
            q.append([u, v[1]+1])
        
#i번째 유저가 j 번째 유저들까지 거쳐가는 최소 단계들의 합
def get_num(i):
    ret = 0
    for j in range(1, n+1):
        if i == j: continue
        ret += bfs(i, j)
    return ret

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i] = list(set(graph[i]))

result = []
#1 ~ n 번째 유저에 대해 케빈 베이컨 수 구하기
for i in range(1, n+1):
    result.append((get_num(i), i))    

result.sort()
print(result[0][1])