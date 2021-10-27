from itertools import combinations
INF = int(1e9)

# 입력 받으면서 집, 치킨집의 위치 추출
n, m = map(int, input().split())
home, chicken = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

# 남길 치킨집의 조합 계산
combination = list(combinations(chicken, m))

# 각 조합에 대하여 도시의 치킨 거리 계산 후, 현재의 최솟값과 비교
min_city_distance = INF
for remain_chicken in combination:

    # 해당 조합에 대하여 도시의 치킨 거리 계산
    city_distance = 0
    for x, y in home:
        min_distance = INF
        for i, j in remain_chicken:
            min_distance = min(min_distance, abs(i - x) + abs(j - y))
        city_distance += min_distance

    # 현재의 최솟값과 비교 후 최솟값 저장
    min_city_distance = min(min_city_distance, city_distance)

# 도시의 치킨 거리의 최솟값 출력
print(min_city_distance)




