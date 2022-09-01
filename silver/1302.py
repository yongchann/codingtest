l = [input() for _ in range(int(input()))]
print(min(l, key=lambda x: (-l.count(x), x)))