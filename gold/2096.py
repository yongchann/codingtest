import sys
input = sys.stdin.readline
n = int(input())
n1, n2, n3 = 0, 0, 0
n4, n5, n6 = 0, 0, 0
for _ in range(n):
    a, b, c = map(int, input().split())
    n1, n2, n3 = max(n1, n2) + a, max(n1, n2, n3) + b, max(n2, n3) + c
    n4, n5, n6 = min(n4, n5) + a, min(n4, n5, n6) + b, min(n5, n6) + c

print(max(n1, n2, n3), min(n4, n5, n6))
