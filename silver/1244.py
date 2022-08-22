n = int(input())
switch = [0] + list(map(lambda x: True if x == "1" else False, input().split()))
for _ in range(int(input())):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, n+1, num):
            switch[i] = not switch[i]
    else:
        switch[num] = not switch[num]
        cnt = 1
        while True:
            if (num-cnt < 1 or num+cnt > n) or (switch[num-cnt] != switch[num+cnt]): break
            switch[num-cnt], switch[num+cnt] = not switch[num-cnt], not switch[num-cnt]
            cnt += 1
    
            

switch = list(map(int, switch))[1:]
answer = [switch[i:i+20] for i in range(0, n, 20)]
for i in answer:
    print(*i)