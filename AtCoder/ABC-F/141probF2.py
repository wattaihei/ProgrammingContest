import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

allxor = 0
for a in A:
    allxor ^= a

L = max(A).bit_length()

dp = [[] for _ in range(L+1)]
for a in A:
    b = (a|allxor)^allxor
    if b != 0:
        dp[b.bit_length()-1].append(b)

a1 = 0
for l in reversed(range(L)):
    if not dp[l]: continue
    c = dp[l].pop()
    if not a1&(1<<l):
        a1 ^= c
    for p in dp[l]:
        b = c^p
        if b != 0:
            dp[b.bit_length()-1].append(b)


ans = 2*a1 + allxor
print(ans)