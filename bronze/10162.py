t = int(input())
answer = []
if t % 10 != 0:
    print(-1)
    exit()

else:
    answer.append(t // 300)
    t %= 300
    
    answer.append(t // 60)
    t %= 60
    
    answer.append(t // 10)
    
print(*answer)