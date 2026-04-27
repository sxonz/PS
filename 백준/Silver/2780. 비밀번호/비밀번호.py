for _ in range(int(input())):
    password = [1]*10
    n = int(input())
    for i in range(1, n):
        new = password[::]
        password[0] = new[7]
        password[1] = new[2] + new[4]
        password[2] = sum(new[1:6:2])
        password[3] = new[2] + new[6]
        password[4] = new[1] + new[5] + new[7]
        password[5] = sum(new[2:9:2])
        password[6] = new[3] + new[5] + new[9]
        password[7] = new[4] + new[8] + new[0]
        password[8] = sum(new[5:10:2])
        password[9] = sum(new[6:9:2])

    print(sum(password)%1234567)