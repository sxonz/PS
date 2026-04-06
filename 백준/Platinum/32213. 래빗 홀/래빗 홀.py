# def back(l,d,turn):
#     if l == 1 and d[0] == 0:
#         return 0
#     for i in range(l):
#         if not d[i]:
#             continue
#         r = d[i]
#         for j in range(d[i]):
#             d[i] = j
#             if not back(l,d,1):
#                 d[i] = r
#                 return 1
#         d[i] = r
#     for i in range(l):
#         for j in range(i+1,l):
#             tmp = [d[i]^d[j]]
#             for k in range(l):
#                 if k not in [i,j]:
#                     tmp.append(d[k])
#             if not back(l-1,tmp,0):
#                 return 1
#     return 0

# while True:
#     r = list(map(int,input().split()))
#     print(back(len(r),r,0))


import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    r = 0
    for i in d:
        r ^= i
    if (r == 1 and n%2 == 0) or (r == 0 and n%2):
        print("tweede")
    else:
        print("eerste")