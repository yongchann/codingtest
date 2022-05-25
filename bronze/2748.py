l = [0, 1]
n = int(input())

for _ in range(n-1):
    l.append(l[-1] + l[-2])

print(l[-1])