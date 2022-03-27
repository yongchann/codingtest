n = int(input())
l = [str(i) for i in range(1,n+1)]
answer = 0

if len(str(n)) == 1:
    answer += n    
else:
    for s in l[9:]:
        #공차 체크해서 인덱스 돌면서 공차랑 다르면 continue
        d = int(s[1]) - int(s[0])
        check = True
        for i in range(1,len(s)):
            if int(s[i]) - int(s[i-1]) != d:
                check = False
                break
        if check :
            answer += 1
         
    answer += 9
    
print(answer)   
