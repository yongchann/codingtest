import sys
input=sys.stdin.readline
dic = {}
for _ in range(int(input())):
    a,b = input().split()
    if b == 'enter':
        dic[a] = 1
    else:
        dic.pop(a)

dic.sort(reverse=True)
for i in dic:
    if i[1]:
        print(i[0])
        
# from collections import defaultdict
# import sys

# n = int(sys.stdin.readline())
# s = defaultdict(int)

# for _ in range(n):
#     a,b = (sys.stdin.readline()).split()
#     if b == 'enter':
#         s[a] += 1
#     elif b == 'leave':
#         del s[a]

# s = sorted(s,reverse=True)

# for i in s:
#     print(i)