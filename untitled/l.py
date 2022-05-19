n = int(input())
answer = []
arr1 = [i for i in range(1, n//2+1)][::-1]
arr2 = [i for i in range(n//2+1, n+1)][::-1]

for i in range(len(arr1)):
    if n%2 == 1:
        answer.append(arr2[i])
        answer.append(arr1[i])
    else:
        answer.append(arr1[i])
        answer.append(arr2[i])
    
if n%2 == 1:
    # print(arr2[-1])
    answer.append(arr2[-1])
    
print(*answer)