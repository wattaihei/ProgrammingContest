import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

D, L, N = map(int, input().split())
C = list(map(int, input().split()))
KFT = [list(map(int, input().split())) for _ in range(N)]

dic = {}
for i, c in enumerate(C):
    if c in dic:
        dic[c].append(i)
    else:
        dic[c] = [i]

dic1 = {}
for num, List in dic.items():
    Pe = []
    t = 0
    for i in range(len(List)-1):
        t += (List[i+1]-List[i]-1)//L + 1
        Pe.append(t)
    t += (List[0]+D-List[-1]-1)//L + 1
    Pe.append(t)
    Po = [Pe[-1]+p for p in Pe]
    dic1[num] = Pe + Po

for K, F, T in KFT:
    F -= 1
    if not K in dic:
        print(0)
    else:
        like = len(dic[K])
        cycle = dic1[K][like-1]
        f_ind = bisect_left(dic[K], F)
        ans = 0
        if f_ind == like:
            T -= (dic[K][0]+D-F+L-1)//L
        elif dic[K][f_ind] != F:
            T -= (dic[K][f_ind]-F+L-1)//L
        if T <= 0:
            print(ans)
        else:
            ans += T//cycle * like
            T %= cycle
            f_ind = (f_ind - 1) % like
            ans += bisect_left(dic1[K], T+dic1[K][f_ind]) - f_ind
            print(ans)