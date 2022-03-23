n = int(input())
l = list(map(int, input().split()))
x = int(input())

answer = 0
left, right = 0, n - 1
l.sort()
while left < right:
    data = l[left] + l[right]
    if data == x:
        answer += 1
        left += 1
        right -= 1
    elif data < x:
        left += 1
    else:
        right -= 1
        
print(answer)