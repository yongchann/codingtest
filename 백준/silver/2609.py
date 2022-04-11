n, m = map(int, input().split())

def gcd(n ,m):
    while m:
        n, m = m, n % m
    return n

print(gcd(n,m))
print(n*m//gcd(n,m))
