n = int(input())
data = [input()[2:].split() for _ in range(n)]
data.sort(key=lambda x: (''.join(x), -len(x)))


def get_pos(i):
    ret = 0
    while ret < len(data[i]) and data[i][ret] == data[i-1][ret]:
        ret += 1
    return ret

print(data)
for i in range(len(data[0])):
    print('--' * i + data[0][i])

#바로 앞에 애랑 시작이 겹치는 갯수 체크
for i in range(1, n):
    pos = get_pos(i)
    if pos != 0:
        for j in range(pos, len(data[i])):
            print('--' * j + data[i][j])
            
    else:
        for j in range(len(data[i])):
            print('--' * j + data[i][j])
            