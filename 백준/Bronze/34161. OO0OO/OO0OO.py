for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                s = (i+1)*1000+j+1
                s -= (l+1)*1000
                if s<=0:
                    s = -1
                print(s)