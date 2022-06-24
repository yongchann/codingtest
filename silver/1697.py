import sys
from collections import deque
n, k = map(int, input().split())
visited = [sys.maxsize] * 1000001

q = deque([n])
visited[n] = 0

while q:
    v = q.popleft()
    
    if v == k:
        print(visited[k])
        break
    
    for i in [v+1, v-1, v*2]:
        if 0<=i<=100000 and visited[v] + 1 < visited[i]:
            q.append(i)
            visited[i] = visited[v] + 1
    
       
    