from collections import Counter
    
t = int(input())
na = int(input())
a = list(map(int, input().split()))
nb = int(input())
b = list(map(int, input().split()))

tableA = [[a[i]] for i in range(na)]
tableB = [[b[i]] for i in range(nb)]

for i in range(na):
    for j in range(i+1, na):
        tableA[i].append(tableA[i][-1] + a[j])
    
for i in range(nb):
    for j in range(i+1, nb):
        tableB[i].append(tableB[i][-1] + b[j])
        
tempA, tempB = [], []
for i in tableA:
    tempA += i
    
for i in tableB:
    tempB += i

l1 = Counter(tempA)
l2 = Counter(tempB)

answer = 0
for i in l1.keys():
    answer += l1[i] * l2[t-i]
print(answer)

# import sys,collections
# input = sys.stdin.readline

# t = int(input())
# a = int(input())
# la = [*map(int,input().split())]
# b = int(input())
# lb = [*map(int,input().split())]

# d = collections.defaultdict(int)
# ans = 0

# for i in range(a):
#     for j in range(i,a):
#         d[sum(la[i:j+1])] += 1
# for i in range(b):
#     for j in range(i,b):
#         ans += d[t-sum(lb[i:j+1])]
# print(ans)