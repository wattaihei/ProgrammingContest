import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
A = [a, b, c, d, a+b, b+c, c+d, a+c, b+d, a+d]
ok = False
S = a+b+c+d
for p in A:
    if S - p == p:
        ok = True
print("YES" if ok else "NO")