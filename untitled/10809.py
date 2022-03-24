s = input()
answer = [-1 for i in range(ord('z') - ord('a'))]

for i in range(len(s)):
    ch = s[i]
    if answer[ord(ch) - ord('a')] == -1:
        answer[ord(ch) - ord('a')] = i
    
print(*answer)