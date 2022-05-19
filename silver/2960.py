n, k = map(int, input().split())
l = [i for i in range(n+1)]
prime = []
l[1] = 0
cnt =0
for i in range(2, int(n**0.5)):
    prime.append(i)
    for j in range(i*2, n+1, i):
        cnt += 1
        l[j] = 0
        
        if cnt == k:
            answer = j
            break
print(answer)