from itertools import combinations
n = int(input())
arr = list(set([input() for _ in range(n)]))
arr.sort(key = lambda x : len(x))

answer = 0
for i in range(n):
    