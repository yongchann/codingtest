n = int(input())
s = input()

data = s[0]
pos = 1
found = False
cnt = 1
while not found and pos < len(s):
    if not found and s[pos] in [chr(ord(data) + 1), chr(ord(data) - 1)]:
        cnt += 1
        
        if cnt == 5:
            found = True
    else:
        cnt = 0
    data = s[pos]
    pos += 1
    
if found :
    print("YES")
else:
    print("NO")