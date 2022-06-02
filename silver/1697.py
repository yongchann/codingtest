from collections import deque
n, m = map(int, input().split())

q = deque([(n, False)])
while q:
    v, level, back = q.popleft()
    if v == m:
        print(level)
        exit()
    
    if not back:
        q.append((v-1, True))
        q.append((v+1, False))
        q.append((v*2, False))
        
    else:
        q.append((v+1, False))
        q.append((v*2, False))


    
    
