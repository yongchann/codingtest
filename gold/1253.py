# from itertools import combinations
# n = int(input())
# l = list(map(int, input().split()))
# answer = 0
# for i in range(len(l)):
#     s = set([i + j for i, j in combinations(l[:i] + l[i+1:], 2)])
#     if l[i] in s: answer += 1
    
# print(answer)

from bisect import bisect_left

n = int(input())
l = sorted(list(map(int, input().split())))
    
s = set()

for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        target = l[i] + l[j]
        pos = bisect_left(l, target)
        
        if pos < len(l) and l[pos] == target and pos not in [i, j]:
            s.add(pos)

print(len(s))
