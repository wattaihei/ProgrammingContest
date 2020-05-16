# AOJ ALDS1_14_B "String Search"
# returns i s.t. S[i+j] = T[j] for 0 <= j < len(T)

def RollingHash(S):
    # gcd(h, b) = 1
    h = 10**11+7
    b = 10**7+7
    L = len(S)

    ret = -1
    hashS = 0
    hashT = 0
    c = 1
    for i in range(L):
        hashS = (hashS * b + ord(S[i])) % h
        hashT = (hashT + ord(S[i])*c) % h
        c = c*b % h
        if hashS == hashT:
            ret = i
    
    return S[:ret+1]


def solve(S):
    T1 = RollingHash(S)
    T2 = RollingHash(S[::-1])
    if len(T1) < len(T2):
        return T2[::-1]
    return T1


import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(input().rstrip()) for _ in range(Q)]

for S in Query:
    N = len(S)
    ind = 0
    while True:
        if S[ind] != S[N-1-ind] or ind >= N-1-ind:
            break
        ind += 1
    R = solve(S[ind:N-ind])
    ans = S[:ind] + R + S[N-ind:]
    print("".join(ans))