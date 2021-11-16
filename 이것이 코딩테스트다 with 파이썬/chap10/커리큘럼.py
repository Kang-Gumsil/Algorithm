from collections import deque
import copy

n = int(input())

# time: 해당 과목의 강의 시간
time = [0] * (n + 1)
in_degree = [0] * (n + 1)

# graph: 해당 과목의 선수 과목
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        in_degree[i] += 1
        graph[j].append(i)

# 해당 과목을 듣기까지 소요되는 시간
result = copy.deepcopy(time)

# 진입 차수가 0인 노드 큐에 넣기
q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    # subject: 해당 과목의 후수 과목들
    for subject in graph[now]:
        result[subject] = max(result[subject], result[now] + time[subject])
        in_degree[subject] -= 1

        if in_degree[subject] == 0:
            q.append(subject)

# 결과 출력
for i in range(1, n + 1):
    print(result[i])


