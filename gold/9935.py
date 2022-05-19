s = list(input())
bomb = list(input())
temp = []
bomb_length = len(bomb)
for i in range(len(s)):
    if temp and temp[-1] == bomb[:-1]:
        if temp[-(bomb_length-1):] + [s[i]] == bomb:
            temp = temp[:-(bomb_length-1)]
    else: temp.append(s[i])
if not temp:
    print('FRULA')
else:
    print(''.join(temp))
    