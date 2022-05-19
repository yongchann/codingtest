n, m = map(int, input().split())
l = list(map(int, input().split()))
start, end = 1, max(l)

# 이중에 정답 무조건 있다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# mid -> 10 
# 20 15 10 17
# 10 5  0  7

while start <= end:
    mid = (start + end) // 2
    get = sum([i - mid if (i - mid) > 0 else 0 for i in l])
    if get >= m:
        start = mid + 1
    else:
        end = mid -1
    
        
print(end)
