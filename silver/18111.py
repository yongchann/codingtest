import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []

for h in range(257):
    #h 보다 높은블럭 인벤토리에 추가 
    temp = b
    add_b, sub_b = 0, 0
    for g in graph:
        for i in g:
            if i > h: add_b += i-h
            elif i < h: sub_b += h-i
    
    if temp + add_b < sub_b:
        continue
    
    time = sub_b + add_b * 2
    answer.append((time, h))
    
answer.sort(key = lambda x : (x[0], -x[1]))

print(*answer[0])