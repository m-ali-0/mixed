import sys

checked = []
stack = []

def dfs(node):
    checked.append(node)
    stack.append(node)
    for neighbor in graph[node]:
        if neighbor not in checked:
            if dfs(neighbor):
                return True
        elif neighbor in stack:
            return True
    stack.pop()
    return False


lines = sys.stdin.read().splitlines()


schedule = []
count = 1
transactions = []

for line in lines:
    if line == 'T':
        current_tr = line + str(count)
        transactions.append(current_tr)
        count+=1
    else:
        time, op = line.split(',')
        time = int(time)
        if 'READ' in op:
            object = op[5]   
            schedule.append((time, current_tr, 'R', object))
        elif 'WRITE' in op:
            object = op[6]
            schedule.append((time, current_tr, 'W', object))
schedule = sorted(schedule)


graph = {key: [] for key in transactions}

for i in range(len(schedule)):
    time1, tr1, op1, ob1 = schedule[i]
    
    for j in range(i+1, len(schedule)):
        time2, tr2, op2, ob2 = schedule[j]
        
        if tr1 != tr2 and ob1 == ob2:
            if 'W' in (op1, op2):
                graph[tr1].append(tr2)
                

for tr in transactions:
    if tr not in checked:
        if dfs(tr):
            print(0)
            exit()
            
print(1)      
            
        
