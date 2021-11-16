def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        i_len = 0

        now = s[:i]
        count = 1

        for j in range(i, len(s), i):
            if now == s[j:j + i]:
                count += 1
            else:
                if count == 1:
                    i_len += i
                else:
                    i_len += len(str(count)) + i

                now = s[j:j + i]
                count = 1

        # 마지막 원소 처리
        if count == 1:
            i_len += len(now)   # 이 경우 i와 len(now)는 다를 수도 있다.
        else:
            i_len += len(str(count)) + i

        answer = min(answer, i_len)

    return answer

