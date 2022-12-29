from collections import deque

floor, start, target, up, down = map(int, input().split())
queue = deque()
depth = 1

queue.append((start+up, start-down, depth))
if start == target:
    print(0)
    exit(0)

visited = []
visited.append(start)
while queue:
    plus, minus, depth = queue.popleft()
    if plus == target or minus == target:
        print(depth)
        exit(0)

    depth += 1
    if 1 <= plus <= floor and plus not in visited:
        visited.append(plus)
        queue.append((plus+up, plus-down, depth))
    if 1 <= minus <= floor and minus not in visited:
        visited.append(minus)
        queue.append((minus+up, minus-down, depth))

print("use the stairs")
