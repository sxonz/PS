for _ in range(int(input())):
    a, b = input().split()
    reversed_a = a[::-1].lstrip('0')
    reversed_b = b[::-1].lstrip('0')
    result = str(int(reversed_a) + int(reversed_b))[::-1].lstrip('0')
    print(result)


