import sys
input = sys.stdin.readline

n, t = map(int, input().split())
carrot = []
for _ in range(n):
    carrot.append(list(map(int, input().split())))
    
carrot.sort(key = lambda x : (x[1], x[0]))
print(sum(carrot[i][0] + carrot[i][1] * (t - n + i) for i in range(n)))    
    