l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()

for i in l:
    str = str.replace(i,'0')
    
print(len(str))