
import sys
input = sys.stdin.readline
from copy import deepcopy

H, W = map(int, input().rstrip().split())
Ss = [list("#" + input().rstrip() + "#") for _ in range(H)]

Ss = [list("#"*(W+2))] + Ss + [list("#"*(W+2))]

ans = 0
for ch in range(1, H+1):
    for cw in range(1, W+1):
        if Ss[ch][cw] == ".": continue
        visited = [[False]*(W+2) for _ in range(H+2)]
        q = [(ch, cw)]
        visited[ch][cw] = True
        while q:
            qq = []
            for h, w in q:
                for nh, nw in [(h+1, w), (h-1, w), (h, w+1), (h, w-1)]:
                    if Ss[nh][nw] == "." and not visited[nh][nw]:
                        visited[nh][nw] = True
                        qq.append((nh, nw))
            q = qq
        
        ok = True
        for h in range(1, H+1):
            for w in range(1, W+1):
                if Ss[h][w] == "." and not visited[h][w]:
                    ok = False
                    break

        if ok: ans += 1

print(ans)