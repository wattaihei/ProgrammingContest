# AOJ ALDS1_14_B "String Search"
# returns i s.t. S[i+j] = T[j] for 0 <= j < len(T)

def RollingHash(S, T, ls):
    if len(S) < len(T):
        return []
    # gcd(h, b) = 1
    h = 10**11+7
    b = 10**7+7
    L = len(T)

    bL = 1
    for i in range(L):
        bL = bL * b % h

    hashS = 0
    for i in range(L):
        hashS = (hashS * b + S[i]) % h

    hashT = 0
    for i in range(L):
        hashT = (hashT * b + T[i]) % h
    
    correctIndexes = [0]*len(S)
    ret = 0
    if hashS == hashT:
        correctIndexes[0] = 1
    for j in range(len(S)-L):
        hashS = (hashS * b - S[j]*bL + S[L+j]) % h
        if hashS == hashT:
            tmp = correctIndexes[j+1-L] + 1
            correctIndexes[j+1] = tmp
            if tmp > ret: ret = tmp
    if ret*L > 2*ls:
        return -1
    return ret


import sys
input = sys.stdin.buffer.readline

S = input().rstrip()
T = input().rstrip()

ls = len(S)
lt = len(T)
S = S*((2*lt+3*ls-1)//ls)
ans = RollingHash(S, T, ls)
print(ans)