# AOJ ALDS1_14_B "String Search"
# returns i s.t. S[i+j] = T[j] for 0 <= j < len(T)
mod = 10**11+7
base = 10**9+7

import sys
input = sys.stdin.buffer.readline

N = int(input())
Ss = [list(input().rstrip()) for _ in range(N)]

Ss.sort(key=lambda x : len(x))

dic = {}
ans = 0
for S in Ss:
    hashS = 0
    s0 = S[0]
    mustConsider = {}

    if hashS in dic:
        for s, c in dic[hashS].items():
            mustConsider[s] = mustConsider.get(s, 0) + c
    for s in S[:0:-1]:
        if s in mustConsider:
            ans += mustConsider[s]
            del mustConsider[s]
        hashS = (base * hashS + s) % mod
        if hashS in dic:
            for s, c in dic[hashS].items():
                mustConsider[s] = mustConsider.get(s, 0) + c
    
    if s0 in mustConsider:
        ans += mustConsider[s0]
        del mustConsider[s0]
    
    if hashS in dic:
        dic[hashS][s0] = dic[hashS].get(s0, 0) + 1
    else:
        dic[hashS] = {s0 : 1}

print(ans)