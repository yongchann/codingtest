from collections import deque
n = int(input())

l = deque([i for i in range(1, n+1)])

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())   
    
print(l[0])