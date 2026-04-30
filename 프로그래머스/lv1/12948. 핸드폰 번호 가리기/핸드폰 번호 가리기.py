def solution(phone_number):
    listnumber = list(str(phone_number))
    starcount = len(listnumber[:-4])
    for i in range(starcount):
        listnumber[i] = '*'
    return ''.join(listnumber)