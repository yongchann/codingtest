n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def possible(route):
    visited = [0] * n
    for i in range(n-1):
        # 같은 높이
        if route[i] == route[i+1]:
            continue
        
        # 높은 높이
        elif route[i]+1 == route[i+1] and i+1 >= l:
            for j in range(i, i-l, -1):
                visited[j] += 1
        
        # 낮은 높이            
        elif route[i]-1 == route[i+1] and i+l < n:
            for j in range(i+1, i+1+l):
                visited[j] += 1
            
        else:
            return False
        
    return max(visited) <= 1

for i in list(zip(*graph)):
    graph.append(list(i))

for route in graph:
    if possible(route):
        answer += 1
    
print(answer)        



