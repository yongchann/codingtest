
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
    
def dfs(node):
    visited[node] = True
    for i, w in graph[node]:
        if not visited[i]:
            distance[i] = distance[node] + w
            dfs(i)
    
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

#1번 노드 기준 제일 먼 곳의 인덱스 찾기
distance = [0] * (n+1)
visited = [False] * (n+1)
dfs(1)

max_index = distance.index(max(distance))

#max_index 기준 제일 먼 곳의 인덱스 찾기
distance = [0] * (n+1)
visited = [False] * (n+1)
dfs(max_index)

print(max(distance))