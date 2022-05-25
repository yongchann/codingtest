import sys
input = sys.stdin.readline
n, m = map(int,input().split())
d = {}
for _ in range(n):
    site, password = input().split()
    d[site] = password

for _ in range(m):
    print(d[input().strip()])