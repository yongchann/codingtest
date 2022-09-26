n, m = map(int, input().split())
info = [tuple(map(int, input().split()))for _ in range(m)]
min_set = sorted(info, key = lambda x: x[0])[0][0]
min_piece = sorted(info, key = lambda x: x[1])[0][1]
answer = 0

answer += min(min_piece * 6, min_set) * (n//6)
answer += min(min_piece * (n % 6), min_set)
print(answer)
