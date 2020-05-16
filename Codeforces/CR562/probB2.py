import sys
input = sys.stdin.readline
from operator import itemgetter

N, M = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

B = [[] for _ in range(N)]
for i, (a1, a2) in enumerate(A):
    B[a1].append(i)
    B[a2].append(i)

def check(x1, x2):
    for a in A:
        if not x1 in a and not x2 in a:
            return False
    return True

C = []
for i in range(N):
    C.append((i, len(B[i])))

C.sort(reverse=True, key=itemgetter(1))
n1 = C[0][0]

ans = 'NO'
if len(B[n1]) == M:
    ans = "YES"
else:
    to_check = [True]*M
    for i in B[n1]:
        to_check[i] = False

    for m in range(M):
        if to_check[m]:
            a1, a2 = A[m]
            break

    if check(n1, a1):
        ans = "YES"
    if check(n1, a2):
        ans = "YES"
    
    i = B[n1][0]
    for k in A[i]:
        if k != n1:
            n2 = k

    to_check = [True]*M
    for i in B[n2]:
        to_check[i] = False

    for m in range(M):
        if to_check[m]:
            a1, a2 = A[m]
            break
    if check(n2, a1):
        ans = "YES"
    if check(n2, a2):
        ans = "YES"


print(ans)