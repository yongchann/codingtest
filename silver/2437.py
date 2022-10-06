n = int(input())
weight = sorted(list(map(int, input().split())))

limit = 0
for w in weight:
    if limit+1 < w:
        break
    limit += w
    
print(limit+1)
        