import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = list([list(map(int, input().split())) for _ in range(n)])
q.sort(key = lambda x : (x[1], x[0]))
q = deque(q)

answer, end = 0, 0
while q:
    begin, finish = q.popleft()
    if begin >= end:
        answer += 1
        end = finish
    
print(answer)