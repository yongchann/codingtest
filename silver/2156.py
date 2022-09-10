n = int(input())
l = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(l))
    exit()
    
dp = [0] * n
dp[0] = l[0]
dp[1] = sum(l[:2])
dp[2] = sum(l[:3]) - min(l[:3])
for i in range(3, n):
    dp[i] = max(dp[i-3] + l[i-1] + l[i], dp[i-1], dp[i-2] + l[i])
print(dp[-1])

# 1 1000 1000 1 1 1 1000 1000 1