# from itertools import permutations
# n = int(input())
# l = [i for i in range(1,n+1)]
# for s in permutations(l):
#     print(*s)



def dfs():
    if len(temp) == n-1:
        print(*temp)    
        return
    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()
            
n = int(input())
temp = []
            
dfs()