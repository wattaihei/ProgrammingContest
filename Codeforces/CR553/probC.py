
mod = 10**9+7
def solve(x):
    if x == 0: return 0
    for K in range(100):
        if 2**K <= x < 2**(K+1):
            break
    score = 0
    if K%2 == 0:
        last1 = 1
        for n in range(K//2):
            last1 += 2*2**(2*n)
        last1 += 2*(x-2**K)
        
        last2 = 0
        for n in range(K//2):
            last2 += 2*2**(2*n+1)

    else:
        last2 = 2
        for n in range(K//2):
            last2 += 2*2**(2*n+1)
        last2 += 2*(x-2**K)

        last1 = -1
        for n in range(K//2+1):
            last1 += 2*2**(2*n)
    score = ((last1+1)**2//4) % mod + ((last2+2)*last2//4) % mod
    score %= mod

    return score

L, R = map(int, input().split())
a = solve(L-1)
b = solve(R)
if b < a:
    b += mod
ans = (b-a)%mod
print(ans)
