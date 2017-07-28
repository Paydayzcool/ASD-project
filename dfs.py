graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start,goal):
    visited, stack = set(), [start]
    pathsTo = {}
    pathsTo[start] = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            for newVertex in (graph[vertex]):
                if newVertex not in visited:
                    if newVertex not in pathsTo:
                        pathsTo[newVertex] = list()
                    for path in pathsTo[vertex]:
                        pathsTo[newVertex].append(path+"->"+newVertex)
                    stack.append(newVertex)
            
            #stack.extend(graph[vertex] - visited)
    for i,j in pathsTo.items():
        #if i == goal:
        print(i,j)
    return visited

dfs(graph, 'A','F')

