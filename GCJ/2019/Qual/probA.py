import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for i, N in enumerate(Query):
    a = 0
    b = 0
    d = 1
    for stn in N[::-1]:
        n = int(stn)
        if n == 4:
            a += 3*d
            b += 1*d
        else:
            a += n*d
        d *= 10
    print("Case #{}:".format(i+1), a, b)