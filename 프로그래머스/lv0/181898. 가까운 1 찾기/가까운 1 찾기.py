def solution(arr, idx):
    return ''.join([str(i) for i in arr]).find('1',idx)