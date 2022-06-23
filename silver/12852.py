n = int(input())
dp1 = [0] * 1000001
dp2 = [[] for _ in range(1000001)]

dp1[1], dp1[2], dp1[3] = 0, 1, 1
dp2[1], dp2[2], dp2[3] = [1], [1,2], [1,3]

for i in range(4, n+1):
    dp1[i] = dp1[i-1] + 1
    dp2[i] = dp2[i-1] + [i]
    
    for j in [2, 3]:
        if i % j == 0 and len(dp2[i]) > len(dp2[i//j])+1:
            dp1[i] = min(dp1[i], dp1[i//j] + 1)
            dp2[i] = dp2[i//j] + [i]
                
print(dp1[n])
print(*reversed(dp2[n]))

# n = int(input())
# dp = [[] for _ in range(n+1)]
# dp[1] = [1]
# for i in range(2, n+1):
#     dp[i] = [i] + dp[i-1]

#     if i % 2 == 0 and len(dp[i//2]) < len(dp[i]):
#         dp[i] = [i] + dp[i//2]

#     if i % 3 == 0 and len(dp[i//3]) < len(dp[i]):
#         dp[i] = [i] + dp[i//3] 

# print(len(dp[-1])-1)
# print(*dp[-1])