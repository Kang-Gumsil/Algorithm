def solution(record):
    answer = []

    # 닉네임 저장하는 딕셔너리 (유저아이디 : 현재닉네임)
    users = {}

    # 최종 닉네임을 알기 위해 하나씩 처리
    for data in record:
        parsed_data = data.split(" ")

        action = parsed_data[0]
        if action == "Leave":
            continue

        uid = parsed_data[1]
        nickname = parsed_data[2]

        users[uid] = nickname

    # 최종 결과 생성
    for data in record:
        parsed_data = data.split(" ")
        
        action = parsed_data[0]
        uid = parsed_data[1]
        nickname = users[uid]

        if action == "Enter":
            answer.append(nickname + "님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(nickname + "님이 나갔습니다.")

    return answer
