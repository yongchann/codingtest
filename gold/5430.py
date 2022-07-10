from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    
    if n == 0:
        q = []
    else:
        q = deque(map(int, input().strip()[1:-1].split(",")))
    
    for cmd in p:
        
        if cmd == 'R':
            q.reverse()
        
        else:
            if not q:
                print('error')
                break
            else:
                q.popleft()
                
    if q:
        print(','.join(q))