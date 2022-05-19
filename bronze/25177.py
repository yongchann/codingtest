from xmlrpc.client import NOT_WELLFORMED_ERROR


n, m = map(int, input().split())
now = list(map(int, input().split()))
present = list(map(int, input().split()))

while len(now) < len(present):
    now.append(0)

answer = max([i-j for i,j in zip(present, now)])
print(answer if answer > 0 else 0)
    