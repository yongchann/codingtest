s = int(input())
temp, i = 1, 1
while temp <= s:
    i += 1
    temp += i
    
print(i-1)