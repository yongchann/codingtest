import bisect
n = int(input())
l = list(map(int, input().split()))
l.sort()
answer = 0
for i in range(n - 1):
    start, end = i, n
    
    while start < end:
        mid = (start + end) // 2
        
        #영역 안에있으면 start를 mid 오른쪽으로 하나씩 늘려감 -> 이분탐색 로직
        if l[mid] <= l[i] / 0.9:
            start = mid + 1
            
        #영역 밖에 있으면 end 를 mid로 당겨옴
        else:
            end = mid
            
    answer += end - i - 1
print(answer)