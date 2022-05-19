import sys, heapq
input = sys.stdin.readline
left = []
right = []

n = int(input().strip())

for _ in range(n):
    data = int(input().strip())
    
    #길이 같으면 왼쪽에 넣고 다르면 오른쪽에 넣기
    
    #넣은후 left[0], right[0] 비교해서 자리바꾸기
    
    if len(left) == len(right):
        heapq.heappush(left, -data)
        
    else:
        heapq.heappush(right, data)
    
    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))
        heapq.heappush(left, -heapq.heappop(right))
        
    print(-left[0])