from itertools import combinations
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
trans_graph = [list(x) for x in zip(*graph)]
final = [[sum(j) for j in zip(graph[i], trans_graph[i])] for i in range(n)]

answer = 987654321
member = set(range(1, n+1))
for team_start in combinations(member, n // 2):
    team_link = list((set(member) - set(team_start)))
    
    score_start, score_link = 0, 0
    
    for i in range(n//2 - 1):
        for j in range(i+1, n//2):
            score_start += final[team_start[i]-1][team_start[j]-1]
            score_link += final[team_link[i]-1][team_link[j]-1]
            
    answer = min(answer, abs(score_start - score_link))

print(answer)


