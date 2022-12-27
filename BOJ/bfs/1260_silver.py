from collections import deque

v, e, start = map(int, input().split())

edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))

# print(edges)

graph = {}

for i in range(1, v+1):
    v_list = []
    for j in range(e):
        if i in edges[j]:
            if i == edges[j][0]:
                v_list.append(edges[j][1])
            else:
                v_list.append(edges[j][0])
    graph[i] = v_list

print(graph)


def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


print(dfs(graph, start))
print(bfs(graph, start))
