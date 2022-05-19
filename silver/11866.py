n, k = map(int, input().split()) 
l = [i for i in range(1,n+1)]
pos, answer = 0, []

while l:
    pos += k - 1
    if pos > len(l) - 1:
        pos %= len(l)
        
    answer.append(l[pos])
    l.pop(pos)

s = '<'+''.join(str(answer))[1:-1] + '>'
print(s)