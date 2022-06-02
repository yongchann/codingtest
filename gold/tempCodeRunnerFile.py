n = int(input())
l = sorted(list(map(int, input().split())))
a, b, c = l[0], sum(l[:2]), sum(l[:3])
if n == 1:
    print(sum(l) - max(l))
elif n == 2:
    print(c * 4 + b * 4)
else:
    one_side = (n-2) * (n-1) * 4 + (n-2) ** 2
    two_side = (n-1) * 4 + (n-2) * 4
    three_side = 4
    
    print(a * one_side + b * two_side + c * three_side)
