import sys
input = sys.stdin.readline

mod = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

bind = M-1
defined = [-1]*M
ans = 1
for i in reversed(range(N)):
    a = A[i]
    if defined[bind] == -1:
        if B[bind] > a:
            ans = 0
            break
        elif B[bind] == a:
            defined[bind] = i
    else:
        if B[bind] > a:
            if bind > 0 and B[bind-1] <= a:
                ans = (ans *  (defined[bind] - i) ) % mod
                if B[bind-1] == a:
                    defined[bind-1] = i
                bind -= 1
            else:
                ans = 0
                break
if bind != 0 or defined[bind] == -1:
    ans = 0
print(ans)