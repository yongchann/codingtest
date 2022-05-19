import heapq
from collections import deque

def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    
    while q:
        cur = q.popleft()

        for i in cur:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                
                
def dfs(graph, visited, start):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,visited,i)
            
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return None 

def dijkstra(graph, dists, start):
    pq = []
    heapq.heappush(pq, (0,start))
    dists[start] = 0
    
    while pq:
        nowDist, now = heapq.heappop(pq)
        
        if dists[now] < nowDist:
           continue
       
        for next , nextCost in graph[now]:
            dist = nowDist + nextCost
            
            if dist < dists[next]:
                dists[next] = dist
                heapq.heappush(pq, (dist,next))

def find(parent, a):
    if a == parent[a]:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(parent, a, b):
    a, b = find(a),  find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b