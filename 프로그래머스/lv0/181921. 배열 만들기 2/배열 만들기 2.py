def solution(l, r):
    temp= [i for i in range(l,r+1) if str(i).count('0')+str(i).count('5') == len(str(i))] 
    return temp if temp else [-1]