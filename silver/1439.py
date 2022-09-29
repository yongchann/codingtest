s = input()
cnt = [0, 0]
now = ""
for i in s:
    if i != now:
        cnt[int(i)] += 1
        now = i
    
print(min(cnt))