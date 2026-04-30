def solution(left, right):
    divisors = []
    answer = 0
    for i in range(left-1, right):
        cnt = [j for j in range(1,i+1) if (i+1) % j == 0]
        cnt.append(i+1)
        divisors.append(cnt)
    for k in range(len(divisors)):
        answer += left + k if len(divisors[k]) % 2 == 0 else 0 - (left+k)
    return answer