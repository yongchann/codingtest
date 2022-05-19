
l = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = list(input())
b = list(input())
lab = []

for i in range(len(a)):
    lab.append(l[ord(a[i]) - ord('A')])
    lab.append(l[ord(b[i]) - ord('A')])

while len(lab) != 2:
    for i in range(len(lab) - 1):
        lab[i] = (lab[i] + lab[i+1]) % 10
    lab.pop()
        
print(str(lab[0]) + str(lab[1]))