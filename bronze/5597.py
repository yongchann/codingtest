l1 = set([int(input()) for _ in range(28)])
l2 = set(list(range(1,31)))

for i in sorted(list(l2-l1)):
    print(i)