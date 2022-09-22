for _ in range(int(input())):
    s = input()
    answer = True
    while answer:
        if len(s) == 1:
            break
        
        left, right = s[:len(s)//2], s[-(len(s)//2):]
        check = all([i != j for i, j in list(zip(left, right[::-1]))])
        
        if check:
            s = left
        else:
            answer = False
            break
        
    print("YES" if answer else "NO")