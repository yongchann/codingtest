import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]

answer = 1
last_max = l.pop()
while l:
    data = l.pop()
    if data > last_max:
        last_max = data
        answer += 1
        
print(answer)