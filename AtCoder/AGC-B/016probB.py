import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
if len(C) == 1:
    X = A[0]
    if N >= 2*X or N == X + 1:
        ans = "Yes"
    else:
        ans = "No"
elif len(C) == 2:
    Xs = sorted(C.keys())
    if Xs[0] + 1 != Xs[1]:
        ans = "No"
    else:
        X = Xs[0]
        if C[X] <= X and C[X+1] >= 2*(X-C[X]+1):
            ans = "Yes"
        else:
            ans = "No"
else:
    ans = "No"

print(ans)