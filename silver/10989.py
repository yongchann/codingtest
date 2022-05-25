# import sys
# input = sys.stdin.readline
# n = int(input())
# from collections import defaultdict
# d = defaultdict(int)

# for _ in range(n):
#     d[int(input())] += 1
    
# l = list(d.items())
# l.sort(key=lambda x : x[0])

# for i in l:
#     for j in range(i[1]):
#         print(i[0])

import sys
input = sys.stdin.readline

n = int(input())
l = [0] * 10001
for _ in range(n):
    l[int(input())] += 1

for i in range(10001):
    if l[i]:
        for j in range(l[i]):
            print(i)