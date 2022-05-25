t = int(input())

for _ in range(t):
    k, n = int(input()), int(input())
    people = [[0] * (n + 1) for _ in range(k+1)]
    people[0] = [i for i in range(n+1)]
    for i in range(1, k + 1):
        for j in range(n + 1):
            people[i][j] = sum(people[i-1][:j+1])

    print(people[k][n])
