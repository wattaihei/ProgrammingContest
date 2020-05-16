import sys
input = sys.stdin.readline
from collections import deque

INF = 10**13

Alp = [chr(i) for i in range(97, 97+26)]

N = int(input())
Ss = [list(input().rstrip()) for _ in range(N)]

for S in Ss:
    ok = True
    defined = [False]*26
    q1 = [S[0]]
    q2 = [S[0]]
    defined[ord(S[0])-97] = True
    now = 0
    for s in S[1:]:
        i = ord(s)-97
        if not defined[i]:
            if now == len(q1)-1:
                q1.append(s)
                defined[i] = True
                now += 1
            elif now == -len(q2)+1:
                q2.append(s)
                defined[i] = True
                now -= 1
            else:
                ok = False
                break
        else:
            if now > 0:
                if q1[now-1] == s:
                    now -= 1
                elif now != len(q1)-1 and q1[now+1] == s:
                    now += 1
                else:
                    ok = False
                    break
            elif now < 0:
                if q2[-now-1] == s:
                    now += 1
                elif now != -len(q2)+1 and q2[-now+1] == s:
                    now -= 1
                else:
                    ok = False
                    break
            else:
                if len(q1) > 1 and q1[1] == s:
                    now = 1
                elif len(q2) > 1 and q2[1] == s:
                    now -= 1
                else:
                    ok = False
                    break
    if not ok:
        print("NO")
    else:
        print("YES")
        for s in Alp:
            if not defined[ord(s)-97]:
                q1.append(s)
        print("".join(q2[::-1] + q1[1:]))