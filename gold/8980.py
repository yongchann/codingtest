n, c = map(int, input().split())
m = int(input())
info = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: (x[1], x[0]))

capacity = [c] * n
answer = 0

for src, dest, box in info:
    can_load = min(box, min(capacity[src:dest]))
    answer += can_load
    
    for i in range(src, dest):
        capacity[i] -= can_load
    
print(answer)