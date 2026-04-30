from math import gcd
def solution(j1,m1,j2,m2):
    m = m1*m2 // gcd(m1,m2)
    j = (j1*m2 // gcd(m1,m2)) + j2*m1 // gcd(m1,m2)
    return (j//gcd(j,m),m//gcd(j,m))