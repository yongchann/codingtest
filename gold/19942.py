from itertools import combinations
n = int(input())
min_nutrition = list(map(int, input().split()))
food_info = list(enumerate([list(map(int, input().split())) for _ in range(n)]))

found, price = False, 987654321
answer = []

for k in range(1, n + 1):
    for data in combinations(food_info, k):
        item, info = zip(*data)
        temp_nutrition = [sum(i) for i in zip(*info)]
        
        if all([i >= j for i, j in zip(temp_nutrition[:-1], min_nutrition)]):
            found = True
            if temp_nutrition[-1] < price:
                price = temp_nutrition[-1]
                answer = item
                
            elif temp_nutrition[-1] == price:
                if ''.join(map(str, answer)) > ''.join(map(str,item)):
                    answer = item                
            
if not found:
    print(-1)
    
else:
    print(price)
    print(*[i+1 for i in answer])