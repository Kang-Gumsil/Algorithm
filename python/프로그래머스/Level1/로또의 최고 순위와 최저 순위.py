def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]  # 당첨 번호와 일치하는 번호의 개수로 순위 찾기
    num_match = 0  # 당첨 번호와 일치하는 번호의 개수

    for num in lottos:
        if num in win_nums:
            num_match += 1

    num_zero = lottos.count(0)  # 알 수 없는 번호의 개수

    return [ranking[num_match + num_zero], ranking[num_match]]
