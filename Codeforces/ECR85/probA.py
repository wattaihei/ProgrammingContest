import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, AB))

for N, AB in Query:
    ok = True
    pa = 0; pb = 0
    for a, b in AB:
        da = a - pa; db = b - pb
        if da < 0 or db < 0 or db > da:
            ok = False
            break
        pa = a
        pb = b
    print("YES" if ok else "NO")