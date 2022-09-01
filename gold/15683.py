n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctvs = [(i, j) for j in range(m) for i in range(n) if 0<graph[i][j]<6]
answer = float("INF")

U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)
types = dict()
types[1] = [[U], [R], [D], [L]]
types[2] = [[U, D], [R, L]]
types[3] = [[U, R], [R, D], [D, L], [L, U]]
types[4] = [[U, R, D], [R, D, L], [D, L, U], [L, U, R]]
types[5] = [[U, R, L, D]]

# cctv_list의 요소는 (cctv 좌표, cctv의 감시 방향벡터)
def get_area(cctv_list):
  ret = [g[:] for g in graph]
  for info in cctv_list:
    y, x = info[0][0], info[0][1]
    vector = info[1]
    
    for dy, dx in vector:
      ny, nx = y + dy, x + dx
      while 0<=ny<n and 0<=nx<m and ret[ny][nx] != 6:
        if ret[ny][nx] == 0:
          ret[ny][nx] = "#"
        ny += dy
        nx += dx
  return ret               

def dfs(cnt, cctv_list):
  global answer
  if cnt == len(cctvs):
    temp = get_area(cctv_list)
    answer = min(answer, sum(t.count(0) for t in temp))
    return
  
  # cnt번 째 cctv의 y, x 좌표
  i, j = cctvs[cnt][0], cctvs[cnt][1]
  direction = types[graph[i][j]]
  for d in direction:
    cctv_list.append([(i, j), d])
    dfs(cnt+1, cctv_list)
    cctv_list.pop()
        
dfs(0, [])
print(answer)