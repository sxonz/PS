def solution(a, d, included):
    array = [a + d*(i-a) for i in range(a,a+len(included))]
    print(array)
    return sum([j for i,j in enumerate(array) if included[i]])