import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
X = list(map(int, input().split()))

if A >= B:
    print(B*(N-1))
else:
    ans = 0
    for i in range(N-1):
        ans += min(A*(X[i+1]-X[i]), B)
    print(ans)