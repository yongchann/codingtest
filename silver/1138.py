from itertools import permutations

n = int(input())
l = list(map(int, input().split()))
# (i번째 사람, 내앞에 나보다 키큰 사람 수)
answer = [0] * n
# 0 0 0 0
for i in range(n):
    cnt, pos = 0, 0
    
    while cnt != l[i]:
        if answer[pos] == 0:
            cnt += 1
        pos += 1
    
    # if answer[pos] == 0 :
    #     answer[pos] = i+1
    
    while answer[pos] != 0:
        pos += 1
    answer[pos] = i+1
    

print(*answer)
# 1 2 3 4
# 2 1 1 0
# 4 2 1 3
