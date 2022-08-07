import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(k, value):
    global answer
    if k > n: return
    answer = max(answer, value)
    for i in range(k, n):
        dfs(i + data[i][0], value + data[i][1])
        
dfs(0, 0)
print(answer)
