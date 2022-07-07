from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

l = []
dl = defaultdict(list)

for _ in range(int(input())):
    data = int(input())
    
    if data != 0:
        heapq.heappush(l, (abs(data), data))
        heapq.heappush(dl[abs(data)], data)
        continue

    if not l:
        print(0)
    else:
        del_data = heapq.heappop(dl[abs(l[0][1])])
        heapq.heappop(l)                    
        print(del_data)
        
