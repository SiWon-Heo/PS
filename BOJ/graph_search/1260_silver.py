# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

# Test Case
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# Answer
# 1 2 4 3
# 1 2 3 4

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
