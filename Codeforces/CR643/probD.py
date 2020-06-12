import sys
input = sys.stdin.readline

N, S = map(int, input().split())

if 2*N <= S:
    print("YES")
    ans = [2]*(N-1) + [S-2*(N-1)]
    print(*ans)
    print(1)
else:
    print("NO")