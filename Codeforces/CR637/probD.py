import sys
input = sys.stdin.readline
from operator import itemgetter

N, K = map(int, input().split())
Ss = [input().rstrip() for _ in range(N)]

Seg = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
nSeg = [int(S, 2) for S in Seg]

def possiblenum(S):
    nS = int(S, 2)
    ret = {}
    for num, T in enumerate(nSeg):
        if T|nS == T:
            need = bin(T^nS).count("1")
            if need in ret:
                ret[need] = max(num, ret[need])
            else:
                ret[need] = num
    return ret

dp = [[-1]*(K+1) for _ in range(N)]
par = [[-1]*(K+1) for _ in range(N)]
que = [0]
for i, S in enumerate(Ss):
    dic = possiblenum(S)
    NUMs = list(dic.items())
    NUMs.sort(key=itemgetter(1), reverse=True)
    qq = []
    for ind in que:
        for need, num in NUMs:
            if ind+need <= K and dp[i][ind+need] == -1:
                dp[i][ind+need] = num
                par[i][ind+need] = ind
                qq.append(ind+need)
    que = qq

if dp[N-1][K] == -1:
    print(-1)
else:
    ind = K
    ans = ""
    for i in reversed(range(N)):
        num = dp[i][ind]
        ind = par[i][ind]
        ans += str(num)
    print(ans[::-1])
