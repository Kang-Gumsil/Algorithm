# 수열을 내림차수능로 정렬하는 프로그램

# N(수열의 크기) 입력 받기
n = int(input())

# N개의 수 입력 받기
arr = []
for _ in range(n):
    arr.append(int(input()))

# 내림차순으로 정렬된 결과를 공백으로 구분하여 출력
arr.sort(reverse=True)
for num in arr:
    print(num, end=' ')
