import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

Alp = [chr(i) for i in range(97, 97+26)]

for n, a, b in Query:
    ans = ""
    for i in range(n):
        ans += Alp[i%b]
    print(ans)