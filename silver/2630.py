import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def solution(y1, x1, y2, x2):
    global white, blue
    hap = sum([l[i][j] for i in range(y1, y2 + 1) for j in range(x1, x2 + 1)])
    if hap == 0:
        white += 1
    elif hap == (y2 - y1 + 1)**2:
        blue += 1
        
    else:
        solution(y1, x1, (y2+y1) // 2, (x2+x1) // 2)
        solution(y1, (x2+x1) // 2 + 1, (y2+y1) // 2, x2)
        solution((y2+y1) // 2 + 1, x1, y2, (x2+x1) // 2)
        solution((y2+y1) // 2 + 1, (x2+x1) // 2 + 1, y2, x2)

solution(0, 0, n - 1, n - 1)

print(white)
print(blue)