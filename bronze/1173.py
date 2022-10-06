N, m, M, T, R = map(int, input().split())
if m + T > M:
    answer = -1
else:    
    now = m
    answer, cnt = 0, 0
    while cnt != N:
        if now + T <= M:
            now += T
            cnt += 1
            
        else:
            now = max(m, now-R)
        answer += 1

print(answer)

