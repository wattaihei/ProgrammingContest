import sys
input = sys.stdin.readline
from collections import Counter

N, K = map(int, input().split())
Ss = [input().rstrip() for _ in range(N)]

D = Counter(Ss)

ans = 0

for v in D.values():
    ans += v*(v-1)*(v-2)//6

p = 0
for i in range(N-1):
    S1 = Ss[i]
    for j in range(i+1, N):
        S2 = Ss[j]
        remain_S = ""
        for k in range(K):
            if S1[k] == S2[k]:
                remain_S += S1[k]
            else:
                for s in 'TES':
                    if s != S1[k] and s != S2[k]:
                        remain_S += s
                        break
        if remain_S in D and remain_S != S1:
            p += D[remain_S]
            
ans += p//3
print(ans)