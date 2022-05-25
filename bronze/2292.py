n = int(input())
# 1
# 2 7 = 5
# 8 19 = 11
# 20 37 = 17
# 38 61 = 23
# 62 91 = 29
# 92
now = 2
layer = 1
while now <= n:
    now += 6*layer
    layer += 1

print(layer)