n = int(input())
five, remain = divmod(n, 5)
answer = -1

if n in [4,7]:
  print(-1)
  exit(0)
if not remain:
  answer = five
else:
  while remain % 3 != 0:
    five -= 1
    remain += 5
  answer = five + remain // 3    
      
print(answer)

