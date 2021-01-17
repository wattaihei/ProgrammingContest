import sys
input = sys.stdin.readline
from operator import itemgetter


H, W, K = map(int, input().rstrip().split())
Ss = [list(input().rstrip()) for _ in range(H)]

ans = 1
for ch in range(H):
    for cw in range(W):
        dic = {Ss[ch][cw] : 1}
        for n in range(2, min(H-ch, W-cw)+1):
            for h in range(ch, ch+n):
                s = Ss[h][cw+n-1]
                dic[s] = dic.get(s, 0) + 1
            for w in range(cw, cw+n-1):
                s = Ss[ch+n-1][w]
                dic[s] = dic.get(s, 0) + 1

            m = max(dic.values())
            if m+K >= n*n:
                ans = max(ans, n)
            else:
                break
print(ans)