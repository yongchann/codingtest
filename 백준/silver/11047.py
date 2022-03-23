n,remain = map(int, input().split())
a = [int(input()) for _ in range(n)]

answer = 0
for i in a[::-1]:
    cnt = remain // i
    answer += cnt
    remain -= cnt * i
    
print(answer)