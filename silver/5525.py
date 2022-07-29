n = int(input())
m = int(input())
s = input()
answer = 0
i = 0
cnt = 0
while i < m-1:
    temp = s[i:i+3]
    if temp == 'IOI':
        i += 2
        cnt += 1
        
        if cnt == n:
            answer += 1
            cnt -= 1
    
    else:
        i += 1
        cnt = 0

print(answer)