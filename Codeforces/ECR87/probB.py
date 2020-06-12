import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    Query.append(list(input().rstrip()))

for S in Query:
    Last = [-1]*3
    ans = 10**16
    for i, s in enumerate(S):
        n = int(s)-1
        Last[n] = i
        if Last[0] != -1 and Last[1] != -1 and Last[2] != -1:
            ans = min(ans, max(Last)-min(Last)+1)
    if ans == 10**16:
        print(0)
    else:
        print(ans)