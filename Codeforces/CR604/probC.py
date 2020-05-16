import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    B = []
    b = 0
    pre = A[0]
    for a in A:
        if a == pre:
            b += 1
        else:
            B.append(b)
            b = 1
        pre = a
    if b > 0:
        B.append(b)
    
    H = N//2
    if len(B) < 3:
        print(0, 0, 0)
    else:
        a1 = B[0]
        a2 = B[1]
        sa = 1
        for i in range(2, len(B)):
            if a2 > a1:
                break
            a2 += B[i]
            sa = i
        if sa == len(B)-1:
            print(0, 0, 0)
        else:
            a3 = B[sa+1]
            s = a1+a2+a3
            if s > H:
                print(0, 0, 0)
            else:
                for i in range(sa+2, len(B)):
                    if s + B[i] > H:
                        break
                    else:
                        a3 += B[i]
                        s += B[i]
                if a3 <= a1:
                    print(0, 0, 0)
                else:
                    print(a1, a2, a3)