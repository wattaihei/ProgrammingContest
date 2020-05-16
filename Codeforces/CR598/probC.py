import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
C = list(map(int, input().split()))

L = sum(C)+(M+1)*(D-1)
if L < N:
    print('NO')
else:
    print('YES')
    rem = L - N
    water = []
    for i in range(M+1):
        if rem >= D-1:
            water.append(0)
            rem -= D-1
        elif rem > 0:
            water.append(D-1-rem)
            rem = 0
        else:
            water.append(D-1)
    ans = []
    for i in range(M):
        ans += [0]*water[i]
        ans += [i+1]*C[i]
    ans += [0]*water[M]
    for a in ans:
        print(a, end=' ')
    print()