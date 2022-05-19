S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = ''.join(reversed(list(T)))
    
    
answer = 1 if S == T else 0
print(answer)