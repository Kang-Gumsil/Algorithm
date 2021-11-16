import math

pos = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    0: [3, 1],
}


def solution(numbers, hand):
    if hand == "left":
        hand = "L"
    else:
        hand = "R"

    # 왼/오 위치
    cur = [[3, 0], [3, 2]]
    answer = ''

    # 하나씩 처리
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
        elif number in [3, 6, 9]:
            answer += 'R'
        else:
            l_dist = get_distance(cur[0], pos[number])
            r_dist = get_distance(cur[1], pos[number])

            if l_dist > r_dist:
                answer += 'R'
            elif l_dist < r_dist:
                answer += 'L'
            else:
                answer += hand

        if answer[-1] == 'L':
            cur[0] = pos[number]
        else:
            cur[1] = pos[number]

    return answer


# 어차피 비교만을 위한 거리 계산이므로 루트까지는 안함
def get_distance(cur, goal):
    return abs(cur[0] - goal[0]) + abs(cur[1] - goal[1])
