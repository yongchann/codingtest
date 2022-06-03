import sys
input = sys.stdin.readline
t = int(input())


for _ in range(t):
    n = int(input())
    l = [input().strip() for _ in range(n)]
    l.sort()
    found = False

    for i in range(n - 1):
        if found:
            break
        if l[i+1].startswith(l[i]):
            found = True            
            print('NO')
            
    if not found:
        print("YES")


