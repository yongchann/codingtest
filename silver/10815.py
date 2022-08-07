n = int(input())
s = set(list(map(int, input().split())))
m = int(input())
answer = [1 if i in s else 0 for i in list(map(int, input().split()))]
print(*answer)