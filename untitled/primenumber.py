# n까지의 소수 구하기
import math
n = int(input())
arr = [i for i in range(n+1)]

def prime_number(n):
    for i in range(2, int(math.sqrt(n))):
        if arr[i] == 0 :
            continue
        
        for j in range(i*2, n+1, i):
            arr[j] = 0
            
    return [i for i in range(2,n+1) if arr[i]]
            
print(prime_number(n))