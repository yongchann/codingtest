from collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque([(1, 1)])
d = 0
answer = 0

n = int(input())
apple = [[False] * (n+1) for _ in range(n+1)]
for _ in range(int(input())):
    y, x = map(int, input().split())
    apple[y][x] = True
    
info = deque([(input().split()) for _ in range(int(input()))])
while True:
    answer += 1
    next_y = snake[-1][0] + direction[d][0]
    next_x = snake[-1][1] + direction[d][1]
    if not (0<next_y<=n and 0<next_x<=n) or (next_y, next_x) in set(snake):
        break
    
    if apple[next_y][next_x]: 
        apple[next_y][next_x] = False
    else:
        snake.popleft()
    
    snake.append((next_y, next_x))
    if info and answer == int(info[0][0]):
        x, c = info.popleft()
        if c == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        
print(answer)