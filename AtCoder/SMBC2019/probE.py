import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7
ans = 1
P = [0, 0, 0]
for a in A:
    c = P.count(a)
    ans = ans*c%mod
    for i in range(3):
        if P[i] == a:
            P[i] += 1
            break
    #print(P)
print(ans)