t = int(input())
while t:
    t -= 1
    h, w, n = map(int, input().split())
    
    if n % h == 0:
        a, b = h, n // h
    else:
        a, b = n%h, n//h + 1
    
    if len(str(b)) == 1:
        print(str(a) + '0' + str(b))
    else:
        print(str(a)+str(b))    
    