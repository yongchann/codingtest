import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
actual = list(range(1,n+1))
print(sum([abs(x - y) for x, y in zip(l, actual)]))
