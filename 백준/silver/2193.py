dp = [0, 1, 1]
for i in range(3, 91):
    s = dp[i - 1] + dp[i - 2]
    dp.append(s)
    
n = int(input())
print(dp[n])