from collections import deque

graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c': ['e'],
    'd' : ['f'],
    'e': [],
    'f': []
}

def breadthFirstPrint(graph,start):
    q = deque([start])

    while q:
        current = q.popleft()

        print(current, end = " ")

        for neighbour in graph[current]:
            q.append(neighbour)

breadthFirstPrint(graph,'a')

