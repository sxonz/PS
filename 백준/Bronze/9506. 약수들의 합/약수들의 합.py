while True:
    n = int(input())
    if n == -1:
        break
    else:
        r = 0
        tmp = str(n) + " = "
        for i in range(1,n//2+1):
            if n % i == 0:
                tmp += str(i) + " + "
                r += i
        if r == n:
            print(tmp[:len(tmp)-2])
        else:
            print(f"{n} is NOT perfect.")