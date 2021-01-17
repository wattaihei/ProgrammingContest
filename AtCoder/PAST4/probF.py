import sys
input = sys.stdin.readline
from operator import itemgetter

N, K = map(int, input().rstrip().split())
Ss = [input().rstrip() for _ in range(N)]

dic = {}
for S in Ss:
    dic[S] = dic.get(S, 0) + 1

L = sorted(dic.items(), key=itemgetter(1), reverse=True)

ac = L[K-1][1]
ans = L[K-1][0]

for i, (s, l) in enumerate(L):
    if i != K-1 and l == ac:
        ans = "AMBIGUOUS"
        break

print(ans)