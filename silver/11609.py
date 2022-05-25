t = int(input())

def check(s):
    l = len(s) // 2
    ret = False
    if len(s) % 2 == 0 and s[:l] == s[l:][::-1]:
            ret = True
    elif s[:l+1] == s[l:][::-1]:
            ret = True
    return ret

for _ in range(t):
    s = input()
    answer = -1
    if check(s):
        answer = 0 
    else:
        left, right = 0, len(s)-1
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        
        if check(s[left:right]) or check(s[left+1:right+1]):
            answer = 1
        else:
            answer = 2

    print(answer)
        