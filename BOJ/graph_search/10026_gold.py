from collections import deque

N = int(input())
board = []
for i in range(N):
    board.append(list(input().rstrip()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

normal_visited = [[0] * N for _ in range(N)]
abnormal_visited = [[0] * N for _ in range(N)]


def bfs(start, color, visited):
    queue = deque([])
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == color and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # print(queue)


# normal
cnt_normal = 0
for i in range(N):
    for j in range(N):
        if normal_visited[i][j] != 1:
            bfs((i, j), board[i][j], normal_visited)
            cnt_normal += 1
# print(cnt_normal)

# abnormal
for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'G'


cnt_abnormal = 0
for i in range(N):
    for j in range(N):
        if abnormal_visited[i][j] != 1:
            bfs((i, j), board[i][j], abnormal_visited)
            cnt_abnormal += 1
# print(cnt_abnormal)

print(cnt_normal, cnt_abnormal)
