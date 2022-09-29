from heapq import heappop, heappush

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
hq = []
info.sort(key=lambda x: x[0])
for i in range(n):
    heappush(hq, info[i][1])
    if len(hq) > info[i][0]:
        heappop(hq)
print(sum(hq))
    