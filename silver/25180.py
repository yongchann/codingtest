l = [0,1,1,1,1,
    1,1,1,1,1,
     2,3,2,3,2,
     3,2,3]

n = int(input())

a, b = divmod(n, 9)

if a % 2 == 1:
    a -= 1 
    b += 9
print(a + l[b])

