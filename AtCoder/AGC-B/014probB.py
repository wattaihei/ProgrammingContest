import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(M):
    a, b = map(int, input().split())
    if not a in dic.keys():
        dic[a] = 1
    else:
        dic[a] += 1
    if not b in dic.keys():
        dic[b] = 1
    else:
        dic[b] += 1

ok = True
for l in dic.values():
    if l % 2 != 0:
        ok = False

if ok:
    print("YES")
else:
    print("NO")