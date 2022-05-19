from collections import deque
gear = [deque(list(input())) for _ in range(4)]
k = int(input())

def left(now, l, dir):
    if l < 0 :
        return 
    if gear[now][6] != gear[l][2]:
        left(l, l-1, -dir)
        gear[l].rotate(-dir)
    
    
def right(now, r, dir):
    if r > 3:
        return
    if gear[now][2] != gear[r][6]:
        right(r, r+1, -dir)
        gear[r].rotate(-dir)

for _ in range(k):
    n, d = map(int, input().split())
    n -= 1
    left(n, n - 1, d)
    right(n, n + 1, d)
    gear[n].rotate(d)
    
answer = 0
for i in range(4):
    if gear[i][0] == '1':
        answer += (2**i)
print(answer)