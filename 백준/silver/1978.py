n = int(input())
a = list(map(int, input().split()))

def getPrime(n):
    check = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            for j in range(i*2, n, i):
                check[j] = False
    
    return [i for i in range(2,n) if check[i]]    
        

prime = getPrime(30)
answer = [i for i in a if i in prime]
print(len(answer))