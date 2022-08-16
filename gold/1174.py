n = int(input())

def dfs(a):
    if a[-1] == '0': return
    
    for i in range(10):
        if a[-1] > str(i):
            temp = a + str(i)
            l.append(temp)
            dfs(temp)
    
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 10):
    dfs(str(i))
    
l = sorted(list(map(int, l)))
print(l[n-1] if n <= len(l) else -1)

    
    
# from itertools import combinations

# n = int(input())
# l = []

# for i in range(1, 11):
#     for num in combinations(list(range(0, 10)), i):
#         num = sorted(list(num), reverse=True)
#         l.append(int("".join(list(map(str, num)))))
        
# l.sort()
# print(l[n-1] if n <= len(l) else -1)