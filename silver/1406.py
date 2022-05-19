from collections import deque
import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = deque([])
m = int(input().strip())

for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'L' :
        if s1 : s2.appendleft(s1.pop())
        
    elif cmd[0] == 'D' :
        if s2 : s1.append(s2.popleft())
    
    elif cmd[0] == 'B' :
        if s1 : s1.pop()

    elif cmd[0] == 'P' :
        s1.append(cmd[1])
        
print(''.join(s1+list(s2)))