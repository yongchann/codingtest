import sys
input = sys.stdin.readline
n, m = map(int, input().split())
from collections import deque
#n * n 리스트, 초기 구름 위치

# 구름을 리스트 말고 N*N 배열로 해서 접근을 상수시간에 해보기

A = [list(map(int, input().split())) for _ in range(n)]
clouds = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])
diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    

def magic(d, s, clouds):
    #이동, 증가
    
    for cloud in clouds:
        cloud[0] += direction[d][0] * s ; cloud[0] %= n
        cloud[1] += direction[d][1] * s ; cloud[1] %= n
        A[cloud[0]][cloud[1]] += 1; 
    
    old = [[False] * n for _ in range(n)]
    for cloud in clouds:
        cnt = 0
        for _dir in diagonal:
            ny = cloud[0] + _dir[0]
            nx = cloud[1] + _dir[1]
            
            if 0<=ny<n and 0<=nx<n and A[ny][nx]:
                cnt += 1
        
        A[cloud[0]][cloud[1]] += cnt
        old[cloud[0]][cloud[1]] = True
        
    
    #clouds 갱신
    clouds.clear()
    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2 and [i, j] and not old[i][j]:
                clouds.append([i,j])
                A[i][j] -= 2
    
    
#m 번의 명령 실행
for _ in range(m):
    d, s = map(int, input().split())
        
    #이동, 1증가, 구름 사라짐, 증가한 칸에서 물복사버그(대각선 물있는 수 만큼 증가), clouds 갱신
    magic(d-1, s, clouds)


print(sum([sum(i) for i in A]))