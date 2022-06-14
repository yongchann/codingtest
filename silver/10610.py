n = sorted(list(input()), reverse = True)
print("".join(n) if n[-1] == '0' and sum([int(i) for i in n[:-1]]) % 3 == 0 else -1)