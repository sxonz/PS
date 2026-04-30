def solution(my_string):
    alphabet_counts = [0] * 52  # 알파벳 개수를 담을 배열 (대문자 A부터 Z, 소문자 a부터 z)

    for char in my_string:
        if 'A' <= char <= 'Z':
            alphabet_counts[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':
            alphabet_counts[ord(char) - ord('a') + 26] += 1

    return alphabet_counts