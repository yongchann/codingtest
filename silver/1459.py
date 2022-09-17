x, y, w, s = map(int, input().split())
answer = 0
if 2*w < s:
    answer += (min(x, y) * 2*w)
else:
    answer += (min(x, y) * s)
remain = abs(x-y)
answer += min(w, s) * 2 * (remain // 2)
if remain % 2:
    answer += w
print(answer)
