n = int(input())
plus, minus= [], []

def solve(arr):
    temp = 0
    while len(arr) >= 2:
        a, b = arr[-1], arr[-2]
        temp += max(a+b, a*b)
        arr = arr[:-2]

    if arr: temp += arr.pop()
    return temp

for _ in range(n):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)
        
plus.sort()
minus.sort(reverse=True)

print(solve(plus) + solve(minus))