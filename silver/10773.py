k = int(input())
l = []
for _ in range(k):
    data = int(input())
    if data:
        l.append(data)
    else:
        l.pop()
print(sum(l))