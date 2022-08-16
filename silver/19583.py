import sys
input = sys.stdin.readline
S, E, Q = input().split()
answer = 0
attend = set()
while True:
    try:
        t, name = input().split()
        if t <= S:
            attend.add(name)
        elif E <= t <= Q and name in attend:
            answer += 1
            attend.remove(name)
    except:
        break
print(answer)