from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(list)
    answer = 1
    for _ in range(int(input())):
        data = input().split()
        d[data[1]].append(data[0])
    
    for l in d.values():
        answer *= (len(l)+1)
    
    print(answer-1)