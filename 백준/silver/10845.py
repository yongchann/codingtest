from sys import stdin
n = int(stdin.readline())
queue = []

for _ in range(n):
    command = stdin.readline().split()
    
    if command[0]  == 'push':
        queue.append(int(command[1]))
        
    elif command[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        res = 0 if queue else 1
        print(res)
        
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            
    