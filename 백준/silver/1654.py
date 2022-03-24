#랜선 자르기
k, n = map(int,input().split())
lans = [int(input()) for _ in range(k)]
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    
    cnt = sum([i//mid for i in lans])
    
    if cnt >= n :
        start = mid + 1
    else:
        end = mid - 1
    
print(end)