def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
            
            
            
            
            
# # 0   0 1 2 3 4 5 6 7
# # -------------------
# # 0 - 1 0 0 0 0 0 0 0
# # 1 - 0 1 0 0 0 0 0 0
# # 2 - 0 0 1 0 0 0 0 0
# # 3 - 0 0 0 1 0 0 0 0
# # 4 - 0 0 0 0 1 0 0 0
# # 5 - 0 0 0 0 0 1 0 0
# # 6 - 0 0 0 0 0 0 1 0
# # 7 - 0 0 0 0 0 0 0 1
# l = []
# for i in range(n, -1, -1):
#     l.append(2**i)

# for _ in range(m):
#     cmd, a, b = map(int, input().split())
#     if cmd == 0:
#         l[a] |= l[b]
#         l[b] |= l[a]
#     else:
#         bin_info = (bin(l[a]))[2:].zfill(n+1)
#         if bin_info[b] == '1': print("YES")
#         else : print("NO")

#비트 마스킹으로 풀이 -> 메모리 초과 
#  n(1 ≤ n ≤ 1,000,000) n 범위만큼의 배열을 만들면 안되는 듯