from itertools import permutations
n = int(input())
l = tuple((map(int, input().split())))

index = list(permutations(l)).index(l)
len = len(list(permutations(l)))
if index + 1 == len:
    print(-1)
else:
    print(*list(permutations(l))[index+1])

