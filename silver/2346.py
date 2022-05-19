from collections import deque
n = int(input())
ballon = list(map(int, input().split()))
index = [i for i in range(1, n + 1)]
info = deque(list(zip(ballon, index)))

print(info)

while info:
    data = info.popleft()
    print(data[1], end = ' ')
    
    #123 -> 231 되어야함 rotate(-)
    if data[0] > 0:
        info.rotate(-(data[0] - 1))
        
    #123 -> 312 되어야함 rotate(+)
    #data[0] < 0 -> -data[0] > 0
    else:
        info.rotate(-data[0])

[(-1, 4), (-1, 5), (2, 2), (1, 3), (5, 6)]


