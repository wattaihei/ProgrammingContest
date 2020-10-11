import sys
import copy
input = sys.stdin.buffer.readline

srtN, lS = input().rstrip().split()
S = list(lS)
N = len(S)
C = {
    ord("A") : 0,
    ord("T") : 0,
    ord("G") : 0,
    ord("C") : 0
}
ans = 0
for i in range(N):
    C[S[i]] += 1
    D = copy.copy(C)
    for j in range(i):
        if D[ord("A")] == D[ord("T")] and D[ord("G")] == D[ord("C")]:
            ans += 1
        D[S[j]] -= 1
print(ans)