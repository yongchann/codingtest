from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))

dp = [a[0]]

for i in a[1:]:
    if i > dp[-1]:
        dp.append(i)
    
    else:
        pos = bisect_left(dp, i)
        dp[pos] = i
    
print(len(dp))
    