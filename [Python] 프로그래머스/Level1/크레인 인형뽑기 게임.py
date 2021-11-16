def solution(board, moves):
    answer = 0
    bucket = []
    n = len(board)

    # 각 열을 스택에 넣기
    data = [[] for _ in range(n + 1)]
    for row in range(n):
        for col in range(n):
            if board[col][row] != 0:
                data[row + 1].append(board[col][row])

    # print_2d(data)
    # 하나씩 계산하기
    for move in moves:
        if not data[move]:
            continue

        cur = data[move].pop(0)
        if bucket and cur == bucket[-1]:
            bucket.pop(-1)
            answer += 2

        else:
            bucket.append(cur)

    return answer


def print_2d(data):
    for row in data:
        for col in row:
            print(col, end=' ')
        print()


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
move = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, move))
