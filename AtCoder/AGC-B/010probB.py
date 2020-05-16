import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

S = sum(A)
ok = True
if S % ((N+1)*N//2) != 0:
    ok = False
else:
    K = S // ((N+1)*N//2)
    c = 0
    for i in range(N):
        a = K-A[i]+A[i-1]
        if a % N != 0:
            ok = False
            break
        x = a // N
        if 0 <= x <= K:
            c += x
        else:
            ok = False
            break
    if c != K:
        ok = False

if ok:
    print('YES')
else:
    print('NO')