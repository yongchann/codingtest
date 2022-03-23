# #순열로 완전탐색은 시간초과
# from itertools import permutations

# n = int(input())
# l = list(map(int, input().split()))
# member = [i for i in range(1, n+1)]
# #(2, 1, 3, 4)
# for case in permutations(member):
#     dict = {}
    
#     for i in range(n):
#         cnt = 0
#         for j in range(i):
#             if case[j] > case[i]:
#                 cnt += 1
#         dict[case[i]] = cnt
        
#     z = sorted(dict.items(), key=lambda x : x[0])
#     ans = [i[1] for i in z]
    
#     if ans == l :
#             print(*case)
    

# n = int(input())
# l = list(map(int, input().split()))
# answer = [1,2,3]
# for i in range(n):
#     print(1)
    
# print(*answer)