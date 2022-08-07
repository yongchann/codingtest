t = int(input())

for i in range(t):
    l = input().split()
    l.reverse()
    print(f"Case #{i+1}:", *l)