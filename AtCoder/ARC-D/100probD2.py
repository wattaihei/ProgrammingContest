import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L = [1, 2, 3]
S = [A[0], A[1], A[2], sum(A[3:])]

ans = max(S) - min(S)
while True:
    if S[2] < S[3] and L[2] < N-1:
        S[2] += A[L[2]]
        S[3] -= A[L[2]]
        L[2] += 1
    elif S[1] < S[2] and L[1] + 1 < L[2]:
        S[1] += A[L[1]]
        S[2] -= A[L[1]]
        L[1] += 1
    elif S[1] < S[2] and L[2] < N-1:
        S[1] += A[L[1]]
        S[2] += A[L[2]] - A[L[1]]
        S[3] -= A[L[2]]
        L[1] += 1
        L[2] += 1
    elif S[0] < S[1] and L[0] + 1 < L[1]:
        S[0] += A[L[0]]
        S[1] -= A[L[0]]
        L[0] += 1
    elif S[0] < S[1] and L[1] + 1 < L[2]:
        S[0] += A[L[0]]
        S[1] += A[L[1]] - A[L[0]]
        S[2] -= A[L[1]]
        L[0] += 1
        L[1] += 1
    elif S[0] < S[1] and L[2] < N-1:
        S[0] += A[L[0]]
        S[1] += A[L[1]] - A[L[0]]
        S[2] += A[L[2]] - A[L[1]]
        S[3] -= A[L[2]]
        L[0] += 1
        L[1] += 1
        L[2] += 1     
    else:
        break
    ans = min(ans, max(S)-min(S))

print(ans)
