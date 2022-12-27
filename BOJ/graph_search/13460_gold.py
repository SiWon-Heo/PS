# 구슬탈출
# https://www.acmicpc.net/problem/13460

row, col = map(int, input().split())

board = []
for _ in range(row):
    board.append(list(map(str, input())))


def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt


for r in range(row):
    for c in range(col):
        if board[r][c] == 'R':
            red_x, red_y = r, c
        if board[r][c] == 'B':
            blue_x, blue_y = r, c
        if board[r][c] == 'O':
            hole_x, hole_y = r, c

# print(board)


def bfs():
    visited = {}
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[(red_x, red_y)] = 1
    s = [[red_x, red_y, blue_x, blue_y, 0]]

    while s:
        rx, ry, bx, by, cnt = s.pop(0)
        if cnt >= 10:
            return -1

        for dx, dy in moves:
            new_red_x, new_red_y, red_cnt = move(rx, ry, dx, dy)
            new_blue_x, new_blue_y, blue_cnt = move(bx, by, dx, dy)

            if board[new_blue_x][new_blue_y] != 'O':
                if new_red_x == hole_x and new_red_y == hole_y:
                    return cnt + 1
                if new_red_x == new_blue_x and new_red_y == new_blue_y:
                    if red_cnt > blue_cnt:
                        new_red_x, new_red_y = new_red_x - dx, new_red_y - dy
                    else:
                        new_blue_x, new_blue_y = new_blue_x - dx, new_blue_y - dy
                if (new_red_x, new_red_y, new_blue_x, new_blue_y) in visited:
                    continue
                else:
                    visited[(new_red_x, new_red_y, new_blue_x, new_blue_y)] = 1
                    s.append(
                        [new_red_x, new_red_y, new_blue_x, new_blue_y, cnt+1])

    return -1


print(bfs())
