from collections import Counter
n = int(input())
l1 = Counter(list(map(int, input().split())))
m = int(input())
l2 = list(map(int, input().split()))

for i in l2:
    print(l1[i], end=' ')