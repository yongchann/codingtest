n, m = map(int,input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
info = list(zip(memory, cost))
info.sort(key = lambda x : -x[0] / x[1] if x[1] != 0 else -1)
print(info)
# now_memory, now_cost = 0, 0
# pos = 0
# while now_memory < m:
#     now_memory += info[pos][0]
#     now_cost += info[pos][1]
#     pos += 1
    

# if now_memory - info[pos-1][0] + info[pos][0] >= m: