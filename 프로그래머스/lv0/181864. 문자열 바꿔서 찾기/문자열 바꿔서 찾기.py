def solution(myString, pat):
    return int(pat in myString.replace('A','Y').replace('B','O').replace('Y','B').replace('O','A'))