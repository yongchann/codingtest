l = [1,1,1,2,2,3,4,5,7,9]
for i in range(10, 101):
    l.append(l[-1] + l[-5])

for _ in range(int(input())):
    print(l[int(input())-1])