n = int(input())
answer = 0
for i in range(n+1):
    temp, cnt = i, 0 
    while temp and temp % 5 == 0:
        temp /= 5
        cnt += 1
    answer += cnt

print(answer)