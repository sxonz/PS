def solution(myString):
    for i in [chr(j) for j in range(97,109)]:
        myString = myString.replace(i,'l')
    return myString