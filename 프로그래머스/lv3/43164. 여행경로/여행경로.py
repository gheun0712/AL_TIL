from collections import defaultdict

answer = []
graph = defaultdict(list)
    
def DFS(s):
    while graph[s]:
        DFS(graph[s].pop(0))
    
    if not graph[s]:
        answer.append(s)
        return

def solution(tickets):

    for start, end in tickets:
        graph[start].append(end)
    
    for start, end in graph.items():
        graph[start].sort()
    
    DFS("ICN")
    
    return answer[::-1]