visited = [[False] * 101 for _ in range(101)]
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
n = int(input())
answer = 0

def get_route(d, g):
    ret = [d]
    for _ in range(g):
        temp = ret[:]
        while temp:
            ret.append((temp.pop() + 1) % 4)
    return ret

for i in range(n):
    x, y, d, g = map(int, input().split())
    visited[y][x] = True
    route = get_route(d, g)
    
    for r in route:
        y += direction[r][0]
        x += direction[r][1]
        visited[y][x] = True
        
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
            answer += 1

print(answer)