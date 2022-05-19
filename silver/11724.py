import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split(' '))
graph = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
            
for i in range(m):
    a,b = map(int,sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    
    
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        dfs(i)
        
print(answer)