# AOJ ALDS1_14_B "String Search"
# returns i s.t. S[i+j] = T[j] for 0 <= j < len(T)

def RollingHash(S, T):
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
        hashS = (hashS * b + ord(S[i])) % h

    hashT = 0
    for i in range(L):
        hashT = (hashT * b + ord(T[i])) % h
    
    correctIndexes = []
    if hashS == hashT:
        correctIndexes.append(0)
    for j in range(len(S)-L):
        hashS = (hashS * b - ord(S[j])*bL + ord(S[L+j])) % h
        if hashS == hashT:
            correctIndexes.append(j+1)
    return correctIndexes

"""
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    S = input().rstrip()
    T = input().rstrip()

    ans = RollingHash(S, T)
    for a in ans:
        print(a)
"""