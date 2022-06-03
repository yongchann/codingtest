s, bomb = input(), input()
st = []

for i in s:
    st.append(i)
    if st[-len(bomb):] == list(bomb):
        for _ in range(len(bomb)):
            st.pop()

if not st:
    print("FRULA")        
else:
    print(''.join(st))