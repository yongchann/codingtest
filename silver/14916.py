n = int(input())

if n in [1, 3]:
    print(-1)
else:
    answer = 0

    n, remain = divmod(n, 5)
    answer += n


    if remain % 2 == 0:
        answer += remain // 2
    
    else:
        answer += (remain+5) // 2 - 1
    
    print(answer)
