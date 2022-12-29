# from collections import deque

# floor, start, target, up, down = map(int, input().split())
# queue = deque()
# depth = 1

# queue.append((start+up, start-down, depth))
# if start == target:
#     print(0)
#     exit(0)

# visited = []
# visited.append(start)
# while queue:
#     plus, minus, depth = queue.popleft()
#     if plus == target or minus == target:
#         print(depth)
#         exit(0)

#     depth += 1
#     if 1 <= plus <= floor and plus not in visited:
#         visited.append(plus)
#         queue.append((plus+up, plus-down, depth))
#     if 1 <= minus <= floor and minus not in visited:
#         visited.append(minus)
#         queue.append((minus+up, minus-down, depth))

# print("use the stairs")

from collections import deque


def bfs(start):
    q = deque([start])

    cnt = [-1] * f
    cnt[start] = 0

    while q:
        cur_floor = q.popleft()

        if cur_floor == g - 1:
            return cnt[cur_floor]

        for i in range(2):
            if i == 0:
                next_floor = cur_floor + u
            else:
                next_floor = cur_floor - d

            if not 0 <= next_floor < f or cnt[next_floor] != -1:
                continue

            q.append(next_floor)
            cnt[next_floor] = cnt[cur_floor] + 1

    return 'use the stairs'


f, s, g, u, d = map(int, input().split())
print(bfs(s - 1))
