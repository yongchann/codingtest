n = int(input())
m = int(input())
s = input()

answer = 0
x = 'IO' * n + 'I'
l = 2*n + 1
while s:
    if s.startswith(x):
        answer += 1
    s = s[1:]
print(answer)