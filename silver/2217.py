import sys
input = sys.stdin.readline
n = int(input())
l = sorted([int(input().strip()) for _ in range(n)], reverse = True)

answer = 0
cnt = 0
for i in range(len(l)):
    cnt += 1
    answer = max(answer, l[i] * cnt)
    
print(answer)