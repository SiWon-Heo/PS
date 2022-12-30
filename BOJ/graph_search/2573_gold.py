from collections import deque
row, col = map(int, input().split())
board = []

for i in range(row):
    board.append(list(map(int, input().split())))

# print(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def update_board():
    zero_count = [[0]*col for _ in range(row)]
    for i in range(1, row-1):
        for j in range(1, col-1):
            cnt = 0
            if board[i+1][j] == 0:
                cnt += 1
            if board[i-1][j] == 0:
                cnt += 1
            if board[i][j+1] == 0:
                cnt += 1
            if board[i][j-1] == 0:
                cnt += 1
            zero_count[i][j] = cnt
    for i in range(1, row-1):
        for j in range(1, col-1):
            board[i][j] = max(board[i][j] - zero_count[i][j], 0)


def dfs(x, y):
    queue = deque([])
    queue.append((x, y))
    while queue:
        # print(queue)
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if board[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


heights = sorted(list(set(sum(board, []))))
# print(heights)

for t in range(300):
    cnt = 0
    visited = [[0]*col for i in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] > 0 and visited[i][j] == 0:
                # for m in range(row):
                #     print(board[m])
                dfs(i, j)
                # print("\n")
                # for m in range(row):
                #     print(visited[m])
                # print("\n")
                cnt += 1
                # print('cnt:', cnt)
                if cnt > 1:
                    print(t)
                    exit(0)
    update_board()
    # print(t)
    # print('sibal')
print(0)
