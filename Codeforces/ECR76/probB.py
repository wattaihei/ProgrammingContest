import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b in Query:
    ok = False
    used = {a}
    while 0 < a < b:
        if a%2 == 0:
            a = a//2 * 3
        elif a > 0:
            a -= 1
        if a in used:
            a = 0
            break
        used.add(a)
    print("YES" if a >= b else "NO")