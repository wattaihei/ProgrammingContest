from fractions import gcd

N = int(input())
T = [int(input()) for _ in range(N)]

def lcm(x, y):
    return (x * y) // gcd(x, y)

ans = T[0]
for t in T:
    ans = lcm(t, ans)

print(ans)