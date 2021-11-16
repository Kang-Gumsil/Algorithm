# 해당 요소가 존재 가능한지에 대한 여부 확인
def possible_exist(x, y, a, arr):
    if a == 0:  # 기둥
        if y == 0 or [x - 1, y, 1] in arr or [x, y, 1] in arr \
                or [x, y - 1, 0] in arr:
            return True

    else:   # 보
        if [x, y - 1, 0] in arr or [x + 1, y - 1, 0] in arr \
                or ([x - 1, y, 1] in arr and [x + 1, y, 1] in arr):
            return True

    return False


# 해당 컴포넌트 삭제 가능한지 확인
def remove(x, y, a, arr):

    # arr 에서 해당 요소를 뺀 다음, 그 리스트의 모든 원소가 가능한지 확인
    tmp_arr = [e for e in arr if e != [x, y, a]]

    for i, j, k in tmp_arr:
        if not possible_exist(i, j, k, tmp_arr):
            return False

    return True


def solution(n, build_frame):
    arr = []

    # build_frame 리스트의 첫 번째 원소부터 확인하며 수행
    for x, y, a, b in build_frame:

        if b == 0:  # 요소 삭제
            if remove(x, y, a, arr):
                arr = [e for e in arr if e != [x, y, a]]

        else:   # 요소 추가
            if possible_exist(x, y, a, arr):
                arr += [[x, y, a]]

    return sorted(arr)


n = 5
frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, frame))



