# 구슬탈출
# https://www.acmicpc.net/problem/13460

# 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

# 각각의 동작에서 공은 동시에 움직인다.
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

# Test case
# 7 7
# #######
# #...RB#
# #.#####
# #.....#
# #####.#
# #O....#
# #######

# answer: 5

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
