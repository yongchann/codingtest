n, m = map(int,(input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
max_hap = 0

def get_comb(y, x, comb):
    print(1)






for i in range(n):
    for j in range(m):
        #get_comb : 가능한 모든 테트로미노 좌표담고있는 리스트
        combs = []
        get_comb(i, j, combs)
        for comb in combs:
            sum = 0
            for k in range(4):
                sum += graph[comb[k][0]][comb[k][1]]
            max_hap = max(max_hap, sum)
            
print(max_hap)