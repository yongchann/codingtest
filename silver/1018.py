n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = 9876543210
chessboard = ['BW'*4 if i % 2 else 'WB'*4 for i in range(8)]

def compare(graph):
    case_b, case_w = 0, 0
    for i in range(8):
        for j in range(8):
            if graph[i][j] != chessboard[i][j]:
                case_b += 1
            else:
                case_w += 1
    return min(case_b, case_w)
    
for i in range(n-7):
    for j in range(m-7):
        temp = []
        for k in range(i, i+8):
            temp.append(board[k][j:j+8])
        answer = min(answer, compare(temp))
        
print(answer)