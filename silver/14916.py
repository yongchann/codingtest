n = int(input())
cnt, remain = divmod(n, 5)
if remain % 2 == 0:
    cnt += remain // 2
    print(cnt)
elif remain % 2 == 1:
    print(-1)

else:
    while remain and cnt:
        temp, remain = divmod(remain+5, 2)
        cnt += temp - 1
    print(cnt)
    