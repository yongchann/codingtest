l = int(input())
s = input()

r, m = 31, 1234567891
s = list(map(lambda x : ord(x) - ord('a') + 1, s))

h = sum([s[i] * r**(i) for i in range(l)]) % m
print(h)