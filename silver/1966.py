from collections import deque
t = int(input())

for _ in range(t):
    n, target = map(int, input().split())
    prior = deque(enumerate(map(int, input().split())))
    cnt = 1
    
    while True:
        if prior[0][1] == max(list(zip(*prior))[1]):
            if prior[0][0] == target:
                print(cnt)
                break
            else:
                prior.popleft()         
                cnt += 1
        
        else:
            prior.append(prior.popleft())