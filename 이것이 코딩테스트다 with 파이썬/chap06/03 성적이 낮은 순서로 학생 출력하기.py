# 학생의 이름과 점수가 주어졌을 때, 점수가 낮은 순서대로 학생으 이름을 출력

# 학생 수 N 입력 받기
n = int(input())

# 학생이름과 점수 입력 받기 (N번)
arr = []
for _ in range(n):
    data = input().split(" ")
    arr.append([data[0], int(data[1])])

# 성적이 낮은 순서대로 학생의 이름 출력
arr.sort(key=lambda x: x[1])
for name, score in arr:
    print(name, end=' ')
