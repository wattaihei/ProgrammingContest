import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A, B, M in Query:
    l = 0
    ok = False
    while B >= (A+M)*2**(l-2):
        if (A+1)*2**l <= B <= (A+M)*2**l:
            ok = True
            break
        l += 1
    if not ok:
        print(-1)
    else:
        ans = []
        b = B
        while b > A:
            ans.append(b)
            if b%2 == 0:
                b //= 2
            else:
                b = b//2 + 1
        ans.append(A)
        L = len(ans)
        print(L, end=' ')
        for i in reversed(range(L)):
            print(ans[i], end=' ')
        print()