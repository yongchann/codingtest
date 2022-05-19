import sys
input = sys.stdin.readline
T = int(input())

while T:
    T -= 1
    s = input().strip()
    left, right = 0, len(s)- 1
    cnt = 0
    while cnt <= 1 and left <= right:
        if s[left] == s[right]:
            left += 1; right -= 1
        else:
          
            if s[left] == s[right-1]:
                left += 1; right -= 2
                cnt += 1
            elif s[left+1] == s[right]:
                left += 2; right -= 1
                cnt += 1
            else:
                cnt = 2
    da
    if cnt == 0: print(0)
    elif cnt == 1: print(1)
    else: print(2)

    #abbab
    #xabba
    
# abbab
# 2
# babba
# 1