from math import ceil
n, l = map(int, input().split())

while True:
    x = (n / l) - ((l - 1) / 2)
    if l > 100 or x <= -1:
        print(-1)
        break
    
    if ceil(x) == x:
        answer = [i for i in range(int(x), int(x)+l)]
        for i in answer:
            print(i,end=' ')
        break
    
    l += 1


    
