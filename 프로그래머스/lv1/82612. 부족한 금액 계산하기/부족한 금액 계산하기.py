def solution(price, money, count):
    totalprice = [i for i in range(1,count+1)]
    totalprice = list(map(lambda x: x * price, totalprice))
    return 0 if sum(totalprice) <= money else sum(totalprice) - money 