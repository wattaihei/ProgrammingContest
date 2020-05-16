import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
L = []
for s in range(1, S+1):
    if s > math.sqrt(S) + 1:
        break
    if S % s == 0:
        L.append(S//s)
        L.append(s)
L.sort(reverse = True)

for l in L:
    T = [a%l for a in A]
    T.sort()
    ans = False
    R = []
    r = 0
    for t in T:
        r += t
        R.append(r)
    #print(l, R)
    for i in range(N):
        #print(i, R[-1])
        if R[i] > K:
            break
        if R[N-1] == l*(N-i-1):
            ans = True
            break
        
    if ans:
        print(l)
        break
