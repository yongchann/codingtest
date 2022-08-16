n, k = map(int, input().split())
num = list(input())
stack = []
cnt = k
for i in range(n):
    while cnt > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        cnt -= 1
    stack.append(num[i])
print(stack)
print("".join(stack[:n-k]))
# print("".join(stack[:n-k]))
# 4177252841
# 417725 2 -> 477252
# 477152 8 -> 772528
# 772528 4 -> 775284
# 775284 1 -> 775841

# 1231234
# 1231 2 -> 2312
# 2312 3 -> 3123
# 3123 4 -> 3234

# 4자리 만들기 = 9683
# 53295683
# 5329 5 -> 5395
# 5395 6 -> 5956
# 5956 8 -> 9568
# 9568 3 -> 9683
