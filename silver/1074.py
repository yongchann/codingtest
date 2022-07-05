n, r, c = map(int, input().split())
value = 0
def find(n, y, x):
    global value
    if n == 1:
        if y == r and x == c:
            return value
        elif y == r and x+1 == c:
            return value + 1
        elif y+1 == r and x == c:
            return value + 2
        else:
            return value + 3
    
    if y<=r<y+2**(n-1) and x<=c<x+2**(n-1):
        return find(n-1, y, x)
        
    elif y<=r<y+2**(n-1) and x+2**(n-1)<=c<x+2**n:
        value += int((2**n)**2 *(1/4))
        return find(n-1, y, x+2**(n-1))
        
    elif y+2**(n-1)<=r<y+2**n and x<=c<x+2**(n-1):
        value += int((2**n)**2 *(2/4))
        return find(n-1, y+2**(n-1), x)
        
    elif y+2**(n-1)<=r<y+2**n and x+2**(n-1)<=c<x+2**n:
        value += int((2**n)**2 *(3/4))
        return find(n-1, y+2**(n-1), x+2**(n-1))
        
    
        

answer = find(n, 0, 0)
print(answer)