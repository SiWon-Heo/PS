from collections import deque

size = int(input())

board = []
for i in range(size):
    board.append(list(map(int, input().split())))

# print(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def bfs(x, y, rain):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if board[nx][ny] < rain:
                continue
            if visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


heights = sorted(list(set(sum(board, []))))
# print(heights)

result = []
for h in heights:
    cnt = 0
    visited = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] >= h and visited[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    result.append(cnt)
print(max(result))
