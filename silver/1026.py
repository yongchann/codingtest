n = int(input())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
print(sum([i*j for i,j in zip(a,b)]))