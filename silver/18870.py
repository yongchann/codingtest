from bisect import bisect_left
n = int(input())
data = list(map(int, input().split()))
answer = []
l = sorted(set(data))
for num in data:
    answer.append(bisect_left(l, num))

print(*answer)