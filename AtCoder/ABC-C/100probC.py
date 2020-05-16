N = int(input())
A = list(map(int, input().split()))

def c2(n):
    c = 0
    while n % 2 == 0:
        n = n // 2
        c += 1
    return c

ans = 0
for a in A:
    ans += c2(a)

print(ans)