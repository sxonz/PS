i = 0
while True:
    i += 1
    a = input()
    b = input()
    if a == "END":
        break
    if sorted(a) == sorted(b):
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")