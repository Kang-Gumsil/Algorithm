allowed = "qwertyuiopasdfghjklzxcvbnm1234567890-_."


def solution(id):
    if not check_id(id):
        id = modify_id(id)

    return id


# 아이디가 규칙에 맞는지 검사
def check_id(id):
    result = True

    if len(id) < 3 or len(id) > 15:
        result = False

    elif list(filter(lambda x: x not in allowed, id)):
        result = False

    elif id[0] == "." or id[-1] == "." or id.count("..") > 0:
        result = False

    return result


# 규칙에 맞는 아이디 생성
def modify_id(id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = id.lower()
    print("1단계:", new_id)

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = "".join(list(filter(lambda x: x in allowed, new_id)))
    print("2단계:", new_id)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while new_id.count("..") > 0:
        new_id = new_id.replace("..", ".")
    print("3단계:", new_id)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]

    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    print("4단계:", new_id)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not new_id:
        new_id = "a"
    print("5단계:", new_id)

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1]
    print("6단계:", new_id)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    len_new_id = len(new_id)
    if len_new_id <= 2:
        new_id += new_id[-1] * (3 - len_new_id)
    print("7단계:", new_id)

    return new_id


new_id = "abcdefghijklmn.p"
print(solution(new_id))