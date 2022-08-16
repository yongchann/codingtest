from collections import defaultdict

n = int(input())
l = list(map(int, input().split()))
d = []
sum_dict = defaultdict(int)
prime = set(range(2, 1000000))
gcd, count = 1, 0

def prime_set(num):
    ret = defaultdict(int)
    temp = num
    for p in prime:
        if p > temp: break
        while temp % p == 0:
            ret[p] += 1
            sum_dict[p] += 1
            temp //= p
    return ret

for i in range(2, int(1000000**0.5)):
    if i in prime:
        for j in range(i+i, 1000000, i):
            if j in prime:
                prime.remove(j)

for i in range(n):
    d.append(prime_set(l[i]))

for k, v in sum_dict.items():
    if v // n <= 0: continue

    gcd *= k**(v//n)
    for i in d:
        if k not in i:
            count += v // n
        
        elif i[k] < v//n:
            count += (v//n - i[k])        
print(gcd, count)