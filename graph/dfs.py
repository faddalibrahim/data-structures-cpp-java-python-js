graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c': ['e'],
    'd' : ['f'],
    'e': [],
    'f': []
}

def depthFirstPrint(graph,start):
    stack = [start]

    

    while stack:
        current = stack.pop()

        if current in visited:
            break


        for neighbour in graph[current]:
            stack.append(neighbour)

def depthFirstRecursive(graph,start):
    print(start,end = " ")
    for neighbour in graph[start]:
        depthFirstRecursive(graph,neighbour)

depthFirstPrint(graph,'a')
depthFirstRecursive(graph,'a')

