n = int(input())
l = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    cnt, pos = 0, 0
    
    while cnt != l[i]:
        if answer[pos] == 0:
            cnt += 1
        pos += 1
    
    while answer[pos] != 0:
        pos += 1
    answer[pos] = i+1
    

print(*answer)
# 1 2 3 4
# 2 1 1 0
# 4 2 1 3