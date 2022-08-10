from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [set() for _ in range(n+1)]
visited = [0] * (n+1)
visited[1] = True
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

q = deque([1])
while q:
    v = q.popleft()
    for i in list(tree[v]):
        if not visited[i]:
            visited[i] = v
            q.append(i)
            
for i in visited[2:]:
    print(i)