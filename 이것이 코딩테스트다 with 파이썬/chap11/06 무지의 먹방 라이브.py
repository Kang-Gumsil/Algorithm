import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i + 1))

    previous = 0
    length = len(q)

    while (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        k -= (now - previous) * length
        previous = now
        length -= 1

    q.sort(key=lambda x: x[1])
    return q[k % length][1]
