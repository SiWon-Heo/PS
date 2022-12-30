from collections import deque
row, col = map(int, input().split())

r, c, d = map(int, input().split())

board = []
for _ in range(row):
    board.append(list(map(int, input().split())))

# for i in range(row):
#     print(board[i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*col for _ in range(row)]

visited[r][c] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]

        d = (d+3) % 4

        if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r, c = nx, ny
                flag = 1
                break
    if flag == 0:
        if board[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]
