str = [input() for _ in range(5)]
answer = ''
for i in range(15):
    for s in str:
        if len(s) >= i + 1:
            answer += s[i]
            
            
print(answer)