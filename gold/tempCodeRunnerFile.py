from collections import deque
import copy
for _ in range(int(input())):
    a, b = input().split()
    first = int(a)
    a = deque(a.rjust(4, '0'))
    b = deque(b.rjust(4, '0'))

    q = deque([[a, '']])
    visited = [False] * 10000
    visited[first] = True

    while q:
        temp, cmd = q.popleft()
        if temp == b:
            print(cmd)
            break

        #cmd D
        D = int(''.join(temp)) * 2 % 10000
        if not visited[D]:
            visited[D] = True
            D = deque(str(D).rjust(4, '0'))
            q.append([D, cmd+'D'])
        
        #cmd S
        S = int(''.join(temp)) - 1
        if not visited[S]:
            if S == 0 : S = 9999
            visited[S] = True
            S = deque(str(S).rjust(4, '0'))
            q.append([S, cmd+'S'])
        
        #cmd L
        L = copy.deepcopy(temp)
        L.rotate(-1)
        l = int(''.join(list(L)))
        if not visited[l]:
            visited[l] = True
            q.append([L, cmd+'L'])
        
        #cmd R
        R = copy.deepcopy(temp)
        
        R.rotate(1)
        r = int(''.join(list(R)))
        if not visited[r]:
            visited[r] = True
            q.append([R, cmd+'R'])