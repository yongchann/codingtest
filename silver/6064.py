t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    visited = [False] * (n+1)
    value = x % n
    cnt = 0
    while True:
        if value == y % n:
            print(cnt * m + x)
            break
        if visited[value]:
            print(-1)
            break
        
        visited[value] = True
        value += m
        value %= n
        cnt += 1
# i = 0
# m,n = 10, 12
# while True:
#     print(i+1, i % m + 1, i % n + 1)
#     if i%m +1 == m and i %n +1 == n:
#         break
#     i+=1