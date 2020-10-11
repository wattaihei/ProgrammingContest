import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = 0
    count = 1
    for a in A:
        if count*a >= X:
            ans += 1
            count = 0
        count += 1
    print(ans)