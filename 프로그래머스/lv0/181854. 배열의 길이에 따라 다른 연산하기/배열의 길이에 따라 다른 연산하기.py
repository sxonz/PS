def solution(arr, n):
    for i,j in enumerate(arr):arr[i] += n * (((len(arr)%2)+i)%2)
    return arr