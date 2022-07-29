import sys
sys.setrecursionlimit(10**9)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = {-1: 0, 0: 0, 1: 0}
def recursion(n, y, x):
    if n == 1:
        answer[graph[y][x]] += 1
        return
    
    check = False
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != graph[y][x]:
                check = True
                break
        if check: break
        
    if not check:
        answer[graph[y][x]] += 1
    else:
        recursion(n//3, y, x)
        recursion(n//3, y, x + n//3)
        recursion(n//3, y, x + n//3 * 2)
        recursion(n//3, y + n//3, x)
        recursion(n//3, y + n//3, x + n//3)
        recursion(n//3, y + n//3, x + n//3 * 2)
        recursion(n//3, y + n//3 * 2, x)
        recursion(n//3, y + n//3 * 2, x + n//3) 
        recursion(n//3, y + n//3 * 2, x + n//3 * 2)
        
                            
recursion(n, 0, 0)

for i in answer.values():
    print(i)