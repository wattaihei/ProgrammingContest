import sys
input = sys.stdin.readline
from collections import Counter

S = input().rstrip()

s_dic = Counter(list(S))

if len(S) < 3:
    if len(S) == 2:
        ans = int(S) % 8 == 0 or int(S[::-1]) % 8 == 0
    else:
        ans = int(S) % 8 == 0
else:
    ans = False
    for i in range(0, 1000, 8):
        a = Counter(list("{:03}".format(i)))
        ok = True
        for s, v in a.items():
            if not s in s_dic or v > s_dic[s]:
                ok = False
        if ok:
            ans = True
            break

print("Yes" if ans else "No")