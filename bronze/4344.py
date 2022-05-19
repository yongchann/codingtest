c = int(input())

while c:
    c -= 1
    data = list(map(int, input().split()))
    n = data[0]
    score = data[1:]
    ave = sum(score) / n
    cnt = 0
    for s in score:
        if s > ave: cnt += 1
    
    rate = cnt/n * 100
    print(f'{rate:.3f}%')