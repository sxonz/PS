def solution(number, limit, power):
    divisor=[0 for i in range(number+1)]
    for i in range(2,number+1):
        for j in range(1,min(number//i+1,i)):
            divisor[i*j]+=2
    for i in range(1,int(number**(1/2))+1):
        divisor[i**2]+=1
    for i,j in enumerate(divisor):
        if j > limit:
            divisor[i] = power
    return sum(divisor)
        