import sys
input = sys.stdin.readline
n, l = int(input()), []
for i in range(n):
    x, r = map(int, input().split())
    l.append((x - r, i, 0))
    l.append((x + r, i, 1))
    
l.sort()
st = []
for i in l:
    if not st and i[2] == 0:
        st.append(i)
        
    elif st and st[-1][0] < i[0] and i[2] == 0:
        st.append(i)
    
    elif st and st[-1][1] == i[1] and st[-1][2] == 0 and i[2] == 1:
        st.pop()

if st:
    print("NO")
else:
    print("YES")