from collections import defaultdict
import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    
    l_min, l_max = [], []
    exist = [False] * 1000001

    for i in range(int(input())):
        cmd, num = input().split()
        num = int(num)
        
        #삽입
        if cmd[0] == 'I':
            # print("\n최소힙에 ", num , " 추가")
            # print("최대힙에 ", num , " 추가")
            # print(i, "번째 명령의 num : " , num , "현재 존재 ! ")
            heapq.heappush(l_min, (num, i))
            heapq.heappush(l_max, (-num, i))
            exist[i] = True
            
        #삭제
        else:
            #최소값 삭제
            if num == -1:
                data = heapq.heappop(l_min)
                # print("최소힙의 루트 삭제합니다")
                # print("root : " , data, 'root 이전에 삭제되었는가? : ', not exist[data[1]])
                # print("최소힙의 루트 : " , data[0])
                while not exist[data[1]]:
                    data = heapq.heappop(l_min)
                exist[data[1]] = False
                # print("삭제 여부 : ", exist[data[1]])
                
                
            #최대값 삭제
            else:
                data = heapq.heappop(l_max)
                # print("최대힙의 루트 삭제합니다")
                # print("root : " , data, 'root 이전에 삭제되었는가? : ', not exist[data[1]])
                # print("최대힙의 루트 : " , -data[0])
                
                while not exist[data[1]]:
                    data = heapq.heappop(l_max)
                exist[data[1]] = False
                # print("삭제 여부 : ", exist[data[1]])
                
                

    if sum(exist) == 0:
        print("EMPTY")
        continue    
    
    
    answer = []
    max_answer = heapq.heappop(l_max)
    
    while not exist[max_answer[1]]:
        max_answer = heapq.heappop(l_max)
    answer.append(-max_answer[0])
    min_answer = heapq.heappop(l_min)
    while not exist[min_answer[1]]:
        min_answer = heapq.heappop(l_min)
    answer.append(min_answer[0])
    
    
    print(*answer)
    
# 1
# 6
# I 3
# I 5
# D -1
# D 1
# I 4
# D -1