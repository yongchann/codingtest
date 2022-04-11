import sys
sys.setrecursionlimit(10**6)
a = [list(input().split()) for _ in range(5)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
nums = []

def dfs(y, x, temp):
    if len(temp) == 6:
        if temp not in nums:
            nums.append(temp)
            return
    
        else:
            temp = temp[:-1]
            return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<5 and 0<=nx<5:
            temp += a[ny][nx]
            dfs(ny, nx, temp)
            temp = temp[:-1]

for y in range(5):
    for x in range(5):
        temp = a[y][x]
        dfs(y, x, temp)      
        
print(len(nums))