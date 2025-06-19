import sys

visited = []
stack = []

def dfs(node):
    visited.append(node)
    stack.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor):
                return True
        elif neighbor in stack:
            return True
    stack.pop()
    return False


lines = sys.stdin.read().splitlines()

print(lines)
print()

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
            letter = op[5]   # after "READ("
            schedule.append((time, current_tr, 'R', letter))
        elif 'WRITE' in op:
            letter = op[6]
            schedule.append((time, current_tr, 'W', letter))
schedule = sorted(schedule)

print(schedule)
print()

graph = {key: [] for key in transactions}

for i in range(len(schedule)):
    time1, tr1, op1, let1 = schedule[i]
    
    for j in range(i+1, len(schedule)):
        time2, tr2, op2, let2 = schedule[j]
        
        if tr1 != tr2 and let1 == let2:
            if 'W' in (op1, op2):
                graph[tr1].append(tr2)
                
print(graph)
print()
print(transactions)

# for x in visited:
#     print(x)

for tr in transactions:
    if tr not in visited:
        if dfs(tr):
            print(0)
            exit()
            
print(1)      
            
        
