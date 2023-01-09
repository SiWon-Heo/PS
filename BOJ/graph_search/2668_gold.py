from collections import defaultdict


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in g[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return


n = int(input().strip())
g = defaultdict(list)
for i in range(1, n+1):
    v = int(input().strip())
    g[v].append(i)

checked = [0 for _ in range(n+1)]
result = []
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for x in result:
    print(x)
