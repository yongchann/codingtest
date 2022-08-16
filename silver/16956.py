import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]



for i in range(n):
    for j in range(m):
        if graph[i][j] =='S':
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0<=ny<n and 0<=nx<m:
                    if graph[ny][nx] == 'W':
                        print(0)
                        exit()
                    
                    elif graph[ny][nx] == '.':
                        graph[ny][nx] = 'D'
print(1)
for i in graph:
    print("".join(i))