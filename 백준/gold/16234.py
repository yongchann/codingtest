import sys
sys.setrecursionlimit(100000)
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

#while문 안에서 l <= (차이) <= r 조건으로 연결영역 구하고 각 영역들 합해서 N빵
#if not 연결영역 : print(answer) break

def dfs(graph, visited, y, x, area):
    visited[y][x] = True
    area.append((y,x))
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and l<=abs(graph[y][x] - graph[ny][nx])<=r:
            area.append((ny, nx))
            dfs(graph, visited, ny, nx, area)
            
    if len(area) == 1:
        area.pop()
        
def get_connected_area(graph, areas):
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            area = []
            if not visited[y][x]:
                dfs(graph, visited, y, x, area)
                
                if len(area) >=1 :
                    areas.append(set(area))


while True:
    #areas = [[(0,0), (0,1), (1,0)], [2,2],[2,3],[3,3], ...]
    areas = []
    get_connected_area(graph, areas)
    
    if not areas:
        print(answer)
        break
    
    answer += 1
    for area in areas:
        if not area:
            continue
        average_area = sum([graph[y][x] for y,x in area]) // len(area)
        for y, x in area:
            graph[y][x] = average_area
        
