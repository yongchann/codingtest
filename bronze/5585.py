n = 1000 - int(input())
answer = 0
for won in [500, 100, 50, 10, 5, 1]:
    answer += n // won
    n %= won
print(answer)