n = int(input())
a = list(enumerate(map(int, input().split())))
a.sort(key=lambda x: x[1])
p = [0]* n 
for i in range(n):
    p[a[i][0]] = i
print(*p)

