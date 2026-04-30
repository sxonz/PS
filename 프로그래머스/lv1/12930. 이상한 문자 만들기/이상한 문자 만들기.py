def solution(s):
    answer = []
    temp = ""
    words = s.split(" ")

    for word in words:
        temp = ""
        for idx, x in enumerate(word):
            if (idx % 2) == 0:
                temp += x.upper()
            else:
                temp += x.lower()
        answer.append(temp)
    return " ".join(answer)