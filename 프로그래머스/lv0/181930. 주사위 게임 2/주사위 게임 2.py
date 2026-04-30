def solution(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b == c:
        return (a*3)*((a*a)*3)*((a*a*a)*3)
    else:
        return (a+b+c)*(a*a+b*b+c*c)