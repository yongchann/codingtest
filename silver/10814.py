from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    a, b = input().split()
    l.append((int(a),b))

answer = sorted(l, key=lambda x : x[0])

for i in answer:
    print(i[0], i[1])
    