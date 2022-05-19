from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque([])
for _ in range(n) :
    cmd = input().split()
    
    if cmd[0] == 'push':
        q.append(cmd[1])
        
    elif cmd[0] == 'pop':
        if len(q) : print(q.popleft())
        else : print(-1)
        
    elif cmd[0] == 'size':
        print(len(q))
        
    elif cmd[0] == 'empty':
        if not len(q) : print(1)
        else : print(0)

    elif cmd[0] == 'front':
        if len(q) : print(q[0])
        else : print(-1)
        
    elif cmd[0] == 'back':
        if len(q) : print(q[-1])
        else : print(-1)
    
    print(q)