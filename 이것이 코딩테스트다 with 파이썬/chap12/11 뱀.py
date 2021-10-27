from collections import deque

n = int(input())
k = int(input())

# 보드를 만들고 사과를 1로 표시
board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 1


# 방향 변환 정보
rotations = deque()
l = int(input())
for _ in range(l):
    x, c = input().split()
    rotations.append((int(x), c))

# 뱀의 좌표 및 머리의 방향 확인
snake = [(1, 1)]
head_for = 1

# 각각 위쪽, 오른쪽, 아래쪽, 왼쪽을 향하고 있을 때 이동할 경우 추가되는 좌표(인덱스)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
rotation = rotations.popleft()
while True:
    time += 1

    # 머리 길이 늘리기
    x, y = snake[0]
    x, y = x + dx[head_for], y + dy[head_for]
    snake = [(x, y)] + snake

    # 머리가 벽에 부딪히면 종료
    if x <= 0 or x > n or y <= 0 or y > n:
        break

    # 자신의 몸과 부딪히면 종료
    if len(set(snake)) != len(snake):
        break

    # 이동한 칸에 사과가 존재하지 않으면 꼬리 제거
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        snake = snake[:-1]

    # 방향 전환 여부 확인
    if time == rotation[0]:
        if rotation[1] == 'L':
            head_for = (head_for - 1) % 4
        else:
            head_for = (head_for + 1) % 4

        if rotations:
            rotation = rotations.popleft()

print(time)
