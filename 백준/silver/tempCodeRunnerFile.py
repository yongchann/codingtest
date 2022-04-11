n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
answer = []

for a in l:
    temp = l.copy()
    temp.remove(a)
    cnt = 0
    for b in temp:
        if a[0] < b[0] and a[1] < b[1]:
            cnt += 1
            
    answer.append(cnt+1)

print(*answer)
