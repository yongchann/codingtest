import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = set(input().split()[1:])

party = []
for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if truth & p:
            truth |= p

answer = 0
for p in party:
    if not p.intersection(truth):
        answer += 1
        
print(answer)


# 순차적으로 진행하면서 진실만을 알아야하는 사람의 수가 늘어남
# 나중에 추가된 진실만을 알아야하는 사람과 이전에 같은 파티에 참석한 사람은 업데이트 안됨
# 순서에 무관한 노드정보를 담아야함 -> 유니온 파인드로 grouping


# def find(x):
#     if x == parent[x]:
#         return x
    
#     return find(parent[x])

# def union(a, b):
#     a = find(a)
#     b = find(b)
    
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# import sys
# input = sys.stdin.readline
        
# n, m = map(int, input().split())
# parent = [i for i in range(n + 1)]
# # 0 1 2 3 4

# # 진실만을 들어야하는 멤버를 모두 0(안쓰는 값)을 최상위 부모로 갖게 만들기
# truth = list(map(int, input()[2:].split()))

# for t in truth:
#     parent[t] = 0
    
# party = []
# for _ in range(m):
#     l = list(map(int, (input()[2:]).split()))
#     party.append(l)
#     if len(l) == 1:
#         continue
#     for i in range(1, len(l)):
#         union(l[0], l[i])
    
# disable_lie = set([i for i in range(1, n + 1) if parent[i] == 0])

# answer = 0
# for p in party:
#     if not set(p).intersection(disable_lie):
#         answer += 1
        
# print(answer)