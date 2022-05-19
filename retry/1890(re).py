n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

