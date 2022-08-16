def dfs(a):
    if a[-1] == '0':
        return
    for i in range(10):
        if a[-1] > num[i]:
            temp = a + num[i]
            l.append(temp)
            dfs(temp)
    
num = "0123456789"
l = [0, 1, 2, 3, 4, 5, 6,7, 8, 9]

for i in range(0, 10):
    dfs(num[i])
l = list(map(int, l))
l.sort()

n = int(input())
if n > len(l):
    print(-1)
else:
    print(l[n])