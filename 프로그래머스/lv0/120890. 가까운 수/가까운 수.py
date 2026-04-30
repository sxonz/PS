def solution(array, n):
    lst0 = [abs(num - n) for num in array]
    if lst0.count(min(lst0)) > 1:
        idx0 = lst0.index(min(lst0), 0)
        idx1 = lst0.index(min(lst0), idx0 + 1)
        return min(array[idx0], array[idx1])
    return array[lst0.index(min(lst0))]