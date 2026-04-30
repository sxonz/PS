def solution(arr, i):
    i[0],i[1] = arr[i[0][0]:i[0][1]+1],arr[i[1][0]:i[1][1]+1]
    i[0].extend(i[1])
    return i[0]