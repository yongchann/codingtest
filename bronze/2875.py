n, m, k = map(int, input().split())
t = 0
while n>= 2 and m >= 1 :
    n -= 2
    m -= 1
    t += 1
        
remain = n + m
while remain < k:
    t -= 1
    remain += 3
    
print(t)
            
