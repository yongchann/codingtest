n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cleaned = [[False] * m for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 1
cleaned[y][x] = True

def check_wall():
    global y, x
    temp_d = (d-2) % 4
    ny = y + direction[temp_d][0]
    nx = x + direction[temp_d][1]
    if graph[ny][nx] == 1: 
        return True
    y, x = ny, nx
    return False

while True:
    for i in range(4):
        d = (d-1) % 4
        ny = y + direction[d][0]
        nx = x + direction[d][1]
        if 1<=ny<n-1 and 1<=nx<m-1 and not cleaned[ny][nx] and not graph[ny][nx]:
            y, x = ny, nx
            cleaned[y][x] = True
            answer += 1
            break
            
    else:
        if check_wall():
            break
        
print(answer)