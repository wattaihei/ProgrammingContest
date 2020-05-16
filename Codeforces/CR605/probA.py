import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, c in Query:
    ans = 10**15
    for n1 in range(a-1, a+2):
        for n2 in range(b-1, b+2):
            for n3 in range(c-1, c+2):
                ans = min(ans, abs(n1-n2) + abs(n2-n3) + abs(n3-n1))
    print(ans)