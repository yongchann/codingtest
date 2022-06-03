import math
s = input()
for i in range(math.ceil(len(s) // 10) + 1):
    print(s[i * 10:i * 10 + 10])