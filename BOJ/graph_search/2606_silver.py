from collections import deque

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
# print(graph)
for _ in range(e):
    edge = input().split()
    graph[int(edge[0])].append(int(edge[1]))
    graph[int(edge[1])].append(int(edge[0]))

# print(graph)


def bfs(graph, start):
    queue = deque()
    visited = []
    for i in range(len(graph[start])):
        queue.append(graph[start][i])
    visited.append(start)
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for j in range(len(graph[n])):
                queue.append(graph[n][j])
    return len(visited)


print(bfs(graph, 1) - 1)
