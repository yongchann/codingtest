from math import factorial

T = int(input())

while T:
    T -= 1
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(m - n) * factorial(n)))