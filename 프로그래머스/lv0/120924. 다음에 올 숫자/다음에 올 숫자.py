def solution(arr):
    temp = [arr[i+1]-arr[i] for i in range(len(arr)-1)]
    if sum([temp[i]-temp[i-1] for i in range(len(temp)-1)]) == 0:
        return arr[-1] + temp[0]
    return arr[-1] * (arr[-1] // arr[-2])