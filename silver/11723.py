import sys
input = sys.stdin.readline
s = set()
m = int(input())
for _ in range(m):
    cmd = input().strip().split()
    if cmd[0] == "add":
        s.add(int(cmd[1]))
            
    elif cmd[0] == "check":
        if 1<= int(cmd[1]) <= 20:
            print(1 if int(cmd[1]) in s else 0)
        
    elif cmd[0] == "remove":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
    
    elif cmd[0] == "toggle":
        if 1<= int(cmd[1]) <= 20:
            if int(cmd[1]) in s: s.remove(int(cmd[1]))
            else: s.add(int(cmd[1]))
    
    elif cmd[0] == "all":
        s = {i for i in range(1, 21)}
    
    elif cmd[0] == "empty": 
        s.clear()
