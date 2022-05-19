from collections import deque
n, k = map(int, input().split())

l = deque([i for i in range(1,n + 1)])

# 1 2 3 4 5 6 7
answer = []

for _ in range(n):
    for __ in range(k-1):
        l.append(l.popleft())
        
    answer.append(l.popleft())

print('<' + (str(answer))[1:-1] + '>')
