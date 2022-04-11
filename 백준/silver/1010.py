T = int(input())

while T:
    T -= 1
    n, m = map(int, input().split())
    up, down = 1, 1
    if n == 1:
        print(m)
        continue
    for i in range(0, n):
        up *= m 
        down *= n - i
    print(up // down)