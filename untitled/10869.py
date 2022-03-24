a, b = input().split()

def rev(s):
    return int(''.join(reversed(list(str(s)))))

print(rev(rev(a) + rev(b)))