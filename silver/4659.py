from collections import deque
import sys
input = sys.stdin.readline

def isV(c):
    return c in list('aeiou')

while True:
    s = input().strip()
    check = True
    if s == 'end':
        break
    
    if all(c not in s for c in 'aeiou'):
        check = False
    
    if check:
        temp = deque(list(s))
        while len(temp) >= 3 and check:
            if isV(temp[0]) == isV(temp[1]) == isV(temp[2]):
                check = False
            else: temp.popleft()
    
    if check:
        temp = deque(list(s))
        while len(temp) >= 2 and check:
            if temp[0] == temp[1] and temp[0] not in ['e', 'o']:
                check = False
            else: temp.popleft()
    
    if check:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
            