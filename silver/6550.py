from collections import deque

while True:
    try:
        s, t = input().split()
        s = deque(s)
        for i in range(len(t)):
            if s and t[i] == s[0]:
                s.popleft()
            
        if not s:
            print("Yes")
        else:
            print("No")        
    except:
        break