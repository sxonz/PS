for i in [list(map(int,input().split())) for _ in range(3)]:
    print({0:'E',1:'A',2:'B',3:'C',4:'D'}[i.count(0)])