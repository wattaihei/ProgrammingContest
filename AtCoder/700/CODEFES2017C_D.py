import sys
input = sys.stdin.readline

S = list(input().rstrip())
INF = 10**15

bit = 0
dic = {0 : 0}
for ind, s in enumerate(S):
    bit ^= 1<<(ord(s)-97)
    score = INF
    if bit in dic:
        score = dic[bit] + 1
    for i in range(26):
        nbit = bit^(1<<i)
        if nbit in dic and dic[nbit]+1 < score:
            score = dic[nbit]+1
    if bit in dic and ind != len(S)-1:
        dic[bit] = min(dic[bit], score)
    else:
        dic[bit] = score

print(dic[bit])