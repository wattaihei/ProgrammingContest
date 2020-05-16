import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    if N%4 != 0:
        print("NO")
    else:
        print("YES")
        L = N//4
        A1 = []
        A2 = []
        for l in range(L):
            A1.append(6*l+1)
            A1.append(6*l+5)
            A2.append(6*l+2)
            A2.append(6*l+4)
        ans = A2 + A1
        print(*ans)