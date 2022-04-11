from unicodedata import digit


n = int(input())

def digit_sum(k):
    return k + sum(list(map(int, str(k))))

for i in range(1, 1000001):
    if digit_sum(i) == n:
        print(i)
        break

else:
    print(0)