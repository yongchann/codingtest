t = int(input())
for _ in range(t):
    n = int(input())
    l = [0] * 11
    l[1], l[2], l[3] = 1, 2, 4
    
    for i in range(4, 11):
        l[i] = l[i-3] + l[i-2] + l[i-1]
    
    print(l[n])
    
    