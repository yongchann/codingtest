dn = {}
n = int(input())
ln = list(input().split())

for i in ln:
    dn[i] = True
    
m = int(input())
lm = list(input().split())
for i in lm:
    try:
        dn[i]
    except:
        print('0')
    else:
        print('1')