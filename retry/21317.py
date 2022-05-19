,,,,,,`n = int(input())
l = [i for i in range(n)]
energy = [list(map(int, input().split())) for _ in range(n - 1)]
info = list(zip(l, energy))
k = int(input())

now, dest = 0, n - 1
print('n', n)
print('k', k)
print('info', info)a