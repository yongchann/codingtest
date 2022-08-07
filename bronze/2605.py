n = int(input())
pick = list(map(int, input().split()))
answer = []
for i in range(n):
    temp = []
    for j in range(pick[i]):
        temp.append(answer.pop())
    answer.append(i+1)
    while temp:
        answer.append(temp.pop())
print(*answer)