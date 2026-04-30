def solution(record):
    user_dict = {}  # 유저 아이디와 닉네임을 저장할 딕셔너리
    answer = []     # 최종적으로 반환할 메시지 리스트

    for r in record:
        tokens = r.split()
        action = tokens[0]
        user_id = tokens[1]

        if action == "Enter" or action == "Change":
            user_dict[user_id] = tokens[2]  # 유저 아이디와 닉네임 저장

    for r in record:
        tokens = r.split()
        action = tokens[0]
        user_id = tokens[1]

        if action == "Enter":
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")

    return answer