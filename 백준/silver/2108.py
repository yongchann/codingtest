from collections import Counter
import sys
n = int(input())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
    
l.sort()
#최빈값
l2 = Counter(l).most_common()
most_list = []
for item in l2:
    if item[1] == l2[0][1]:
        most_list.append(item[0])

if len(most_list) >=2:
    most = sorted(most_list)[1]
else:
    most = most_list[0]

print(round(sum(l) / n))
print(l[len(l)//2])
print(most)
print(max(l)-min(l))