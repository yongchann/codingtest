import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
    
l.sort()
s = ''
for i in range(n):
    s += str(l[i])
    s += '\n'

print(s[:-1])