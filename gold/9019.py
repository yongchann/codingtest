from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque([[a, '']])
    visited = [False] * 10000
    visited[a] = True
    while q:
        num, cmd = q.popleft()
        if num == b:
            print(cmd)
            break

        #cmd D
        temp = num * 2 % 10000
        if not visited[temp]:
            q.append([temp, cmd+'D'])
            visited[temp] = True
        
        #cmd S
        temp = (num - 1) % 10000
        if not visited[temp]:
            q.append([temp, cmd+'S'])
            visited[temp] = True
    
        #cmd L
        temp = (num % 1000) * 10 + num // 1000
        if not visited[temp]:
            q.append([temp, cmd+'L'])
            visited[temp] = True
        
        #cmd R
        temp = (num % 10) * 1000 + num // 10
        if not visited[temp]:
            q.append([temp, cmd+'R'])
            visited[temp] = True
            
            
            