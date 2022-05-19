import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    l = sorted([tuple(map(int, input().split())) for _ in range(n)])
    min_rank = l[0][1]
    answer = 1
    
    for i in range(n):
        if l[i][1] < min_rank:
            min_rank = l[i][1]
            answer += 1
            
    print(answer)
        
   