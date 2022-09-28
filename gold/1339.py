from collections import defaultdict

n = int(input())
coefficient = defaultdict(int)

for i in range(n):
    s = input()[::-1]
    for idx, alpha in enumerate(s):
        coefficient[alpha] += (10 ** idx)

result = sorted(coefficient.values(), reverse=True)
answer = 0

for i in range(len(result)):
    answer += (result[i] * (9-i))
    
print(answer)