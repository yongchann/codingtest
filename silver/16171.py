s = input()
target = input()
n = list('0123456789')
for i in n:
    s = s.replace(i, '')
    
if target in s:
    print(1)
else:
    print(0)