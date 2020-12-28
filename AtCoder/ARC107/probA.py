import sys
input = sys.stdin.buffer.readline

mod = 998244353

A, B, C = map(int, input().rstrip().split())
ans = A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2
print(ans%mod)