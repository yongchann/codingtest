import sys
input = sys.stdin.readline

width, height = map(int, input().split())
t = int(input())
v, h = [0,width],[0,height]

for _ in range(t):
    vertical, pos = map(int, input().split())
    if vertical:
        v.append(pos)
    else:
        h.append(pos)
        
v.sort()
h.sort()
print(max([i[0]-i[1] for i in zip(v, [0]+v)]) * max([i[0]-i[1] for i in zip(h, [0]+h)]))