# 시계방향으로 회전
def rotation(arr):
    m = len(arr)
    new_arr = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_arr[i][j] = arr[m - j - 1][i]

    return new_arr


# 좌물쇠의 크기를 기존 크기의 3배로 변환
def extend_three_times(lock):
    n = len(lock)

    # 중앙 부분은 기존 좌물쇠의 값으로, 그 외에는 2로 채우기
    new_lock = [[2] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    return new_lock


# 키의 (0, 0)이 확대된 좌물쇠의 (x, y)에 있을 때 성공여부 확인하기
def check_success(key, lock, x, y):
    m = len(key)
    n = len(lock)

    extended_lock = extend_three_times(lock)
    for i in range(m):
        for j in range(m):
            extended_lock[x + i][y + j] += key[i][j]

    added_lock = [row[n:n * 2] for row in extended_lock[n:n * 2]]
    for i in range(n):
        for j in range(n):
            if added_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 시계 방향으로 회전하면서 4번 시도
    for _ in range(4):
        key = rotation(key)

        # 키의 (0, 0)이 확대된 좌물쇠의 (x, y)에 있을 때 성공여부 확인
        for x in range(n * 2):
            for y in range(n * 2):
                if check_success(key, lock, x, y):
                    return True

    return False