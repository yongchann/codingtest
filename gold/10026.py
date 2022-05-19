import sys
sys.setrecursionlimit(100000)

#문제 입력
n = int(input())
s = [input() for _ in range(n)]
able = [list(i) for i in s]
disable = [list(i.replace('G','R')) for i in s]

#탐색용 단위벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# RGB, RB, RGBYC등 무관하게 같은 색만 탐색을 진행 해 나가기 때문에 graph[ny][nx] == color 체크로 단순하게 풀이 가능
def dfs(graph, visited, y, x):
    visited[y][x] = True
    color = graph[y][x]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx]  and graph[ny][nx] == color:
            dfs(graph, visited, ny, nx)

#dfs 돌면서 visited false 를 만나면 answer += 1
def sol(graph):
    visited = [[False] * n for i in range(n)]
    answer = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                answer += 1
                dfs(graph, visited, y, x)
    return answer


print(sol(able), sol(disable))