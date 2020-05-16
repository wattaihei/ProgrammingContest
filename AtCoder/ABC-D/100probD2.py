import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.append(0)

S = [A[0], A[1], A[2], sum(A[3:])]
l = 0
r = 2
while r < N-1:
    if S[2] + A[r+1] <= S[3] - A[r+1]:
        S[2] += A[r+1]
        S[3] -= A[r+1]
        r += 1
    else:
        break

S2 = [S[0], S[1], S[2]+A[r+1], S[3]-A[r+1]]
ans = min(max(S)-min(S), max(S2)-min(S2))
for m in range(2, N-2):
    S[1] += A[m]
    S[2] -= A[m]
    while r < N-1:
        if S[2] + A[r+1] <= S[3] - A[r+1]:
            S[2] += A[r+1]
            S[3] -= A[r+1]
            r += 1
        else:
            break
    
    while l < m:
        if S[0] + A[l+1] <= S[1] - A[l+1]:
            S[0] += A[l+1]
            S[1] -= A[l+1]
            l += 1
        else:
            break
    
    S1 = [S[0]+A[l+1], S[1]-A[l+1], S[2], S[3]]
    S2 = [S[0], S[1], S[2]+A[r+1], S[3]-A[r+1]]
    S3 = [S[0]+A[l+1], S[1]-A[l+1], S[2]+A[r+1], S[3]-A[r+1]]
    ans = min([ans, max(S)-min(S), max(S1)-min(S1), max(S2)-min(S2), max(S3)-min(S3)])

print(ans)