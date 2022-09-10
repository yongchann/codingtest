n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]
for i in range(n):
    answer[i][i] = 1
            
a = list(bin(b)[2:])
powers_of_two, cnt = [], 1
while a:
    if a.pop() == '1': 
        powers_of_two.append(2**(cnt-1))
    cnt += 1
    
def multiple(a, b):
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = sum(a[i][k] * b[k][j] for k in range(n)) % 1000
    return ret

def recursion(m):
    global answer, matrix
    if m == powers_of_two[-1] * 2:
        return 
    if m in powers_of_two:
        answer = multiple(answer, matrix)
        
    matrix = multiple(matrix, matrix)
    recursion(m*2)
        
recursion(1)
    
for i in answer:
    print(*i)
