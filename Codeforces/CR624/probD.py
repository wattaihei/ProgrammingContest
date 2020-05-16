import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A, B, C in Query:
    ans = 10**15
    for a in range(1, C+1):
        m = 1
        while True:
            b = m*a
            k = C//b
            c = k*b
            if abs(c-C) > abs((k+1)*b-C):
                c = (k+1)*b
            tmp = abs(a-A)+abs(b-B)+abs(c-C)
            if tmp < ans:
                ans = tmp
                E = [a, b, c]
            if b > C:
                break
            m += 1
    print(ans)
    print(*E)