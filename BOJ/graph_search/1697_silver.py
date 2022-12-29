from collections import deque
import math
n, k = map(int, input().split())

queue = deque()
# visited = []
if n == k:
    print(0)
    exit(0)
queue.append((n-1, n+1, 2*n, 1))
depth = 1


def bfs():
    global depth
    visited = [n]
    while queue:
        # print(queue)
        minus, plus, multiple, depth = queue.popleft()
        depth += 1
        if 0 <= minus < 100000 and minus not in visited:
            visited.append(minus)
            queue.append((minus-1, minus+1, 2*minus, depth))
        if 0 <= plus < 100000 and plus not in visited:
            visited.append(plus)
            queue.append((plus-1, plus+1, 2*plus, depth))
        if 0 <= multiple < 100000 and multiple not in visited:
            visited.append(multiple)
            queue.append((multiple-1, multiple+1, 2*multiple, depth))
        if minus == k or plus == k or multiple == k:
            print(depth - 1)
            exit(0)
        visited = sorted(list(set(visited)))
        # print(visited, depth)


bfs()
