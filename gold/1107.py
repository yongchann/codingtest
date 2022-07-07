n = int(input())
m = int(input())
broken_button = set(input().split()) if m else set()
answer = abs(n-100)

for num in range(1000000):
    s = str(num)   
    
    for i in range(len(s)):
        if s[i] in broken_button:
            break
            
        if i == len(s)-1:
            answer = min(answer, abs(num-n) + len(s))
print(answer)