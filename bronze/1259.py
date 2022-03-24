while True:
    a = input()
    if a == '0':
        break
    
    pos = len(a) // 2
    start = a[:pos] if len(a) % 2 == 0 else a[:pos+1]
    end = ''.join(a[pos:][::-1])
    
    if start == end:
        print('yes')
    else:
        print('no')
    