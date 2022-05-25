from collections import deque
n = int(input())
l = [int(input()) for _ in range(n)]
answer, st1, st2 = [] ,[0], deque([i for i in range(1,n+1)])

err = False
for i in l:
    if st1 and st1[-1] > i:
        err = True
        break
    
    while st1[-1] != i:
        st1.append(st2.popleft())
        answer.append('+')
    
    st1.pop()
    answer.append('-')

if err:
    print("NO")

else:
    for i in answer:
        print(i)