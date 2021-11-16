# N개의 원소
# 최대 K번의 바꿔치기
# 배열 A의 합이 최대가 되도록...


# N, K 입력 받기
n, k = map(int, input().split())

# A의 원소들 (N개) 입력 받기
a = list(map(int, input().split()))

# B의 원소들 (N개) 입력 받기
b = list(map(int, input().split()))

# 배열 A의 모든 원소의 합의 최댓값 출력

# A 오름차순 정렬, B 내림차순 정렬
a.sort()
b.sort(reverse=True)

# 인덱스 0부터 A와 B 비교하며 A가 더 크거나 K를 초과하면 종료...
for i in range(k):
    if a[i] > b[i]:
        break
    a[i] = b[i]

print(sum(a))
