import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
    
l.sort(key = lambda x : (x[0], x[1]))

for a in l :
    print(*a)