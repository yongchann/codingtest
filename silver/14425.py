import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set([input().strip() for _ in range(n)])
answer = 0

l = [input().strip() for _ in range(m)]
for i in l:
    if i in s:
        answer += 1
        
print(answer)