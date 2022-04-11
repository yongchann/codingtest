a = list(map(int, list(input())))
b = list(map(int, list(input())))

lab = []

for i in range(len(a)):
    lab.append(a[i])
    lab.append(b[i])

while len(lab) != 2:
    for i in range(len(lab) - 1):
        lab[i] = (lab[i] + lab[i+1]) % 10
    lab.pop()
        
print(str(lab[0]) + str(lab[1]))