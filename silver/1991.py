from collections import defaultdict
n = int(input())
d = defaultdict(list)

for _ in range(n):
    info = input().split()
    d[info[0]].append(info[1])
    d[info[0]].append(info[2])
    

def preOrder(x):
    if x == '.':
        return
    
    print(x, end='')
    preOrder(d[x][0])
    preOrder(d[x][1])


def inOrder(x):
    if x == '.':
        return
    
    inOrder(d[x][0])
    print(x, end='')
    inOrder(d[x][1])

def postOrder(x):
    if x == '.':
        return
    
    postOrder(d[x][0])
    postOrder(d[x][1])
    print(x, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')