n = int(input())
num = list(map(int, input().split()))
answer =[]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if n == 2:
    temp = gcd(num[0], num[1])
    
elif n == 3:
    temp = gcd(gcd(num[0], num[1]), num[2])

#temp = 16

for i in range(1, temp + 1):
    if temp % i == 0:
        answer.append(i)
        

for i in range(len(answer)):
    print(answer[i])