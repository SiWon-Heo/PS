# <그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
# 첫 번째 줄에는 총 단지수를 출력하시오.
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# Test case
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# Answer
# 3
# 7
# 8
# 9

# # 완전탐색 문제이므로 DFS를 쓰는 것이 맞을 듯하다.

# # board에서 시작점들을 찾아야한다. 어떻게하지?
# # 0. cnt = 2
# # 1. 1을 하나 잡아서 완전탐색한다. 탐색이 끝난 애들은 cnt로 바꾼다.
# # 2. 1을 찾는다.
# #   2-1. 1이 없다면 탐색을 끝낸다.
# #   2-2. 아니라면 cnt++, board의 1 중 하나를 잡아서 다시 완전탐색한다.

row = col = int(input())

# print(row, col)

board = []
for i in range(row):
    board.append(list(map(int, input().rstrip())))

# print(board)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(x, y):
    global cnt
    if board[x][y] == 0:
        return 0, 0

    board[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= row or ny < 0 or ny >= col):
            continue
        if board[nx][ny] == 0:
            continue
        cnt += 1
        dfs(nx, ny)
    return 1, cnt+1


res1 = 0
res2 = []
for i in range(row):
    for j in range(col):
        num1, num2 = dfs(i, j)
        if num1 == 0:
            continue
        else:
            res1 += num1
        res2.append(num2)
        cnt = 0

res2.sort()

print(res1)
for i in res2:
    print(i)
