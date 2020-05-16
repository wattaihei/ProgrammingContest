import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

R = [None]*(2*N)
odd = False
for i in range(2*N):
    if S[i] == 'W':
        if odd:
            R[i] = 1
            odd = False
        else:
            R[i] = 0
            odd = True
    else:
        if odd:
            R[i] = 0
            odd = False
        else:
            R[i] = 1
            odd = True
if sum(R) != N:
    print(0)
else:
    ans = 1
    mod = 10**9+7
    num_r = 0
    for i in range(2*N):
        if R[i]:
            num_r += 1
        else:
            ans = (ans*num_r)%mod
            num_r -= 1
    for n in range(1, N+1):
        ans = (ans*n)%mod
    print(ans)