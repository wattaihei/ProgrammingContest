N, A, B = map(int, input().split())

if (A-B)%2 == 0:
    ans = abs(A-B)//2
else:
    d1 = min(A, B) - 1
    r1 = max(A, B) - d1 - 1
    a1 = (r1-1)//2 + 1 + d1

    d2 = N- max(A, B)
    r2 = min(A, B) + d2 + 1
    a2 = (N - r2)//2 + 1 + d2
    ans = min(a1, a2)

print(ans)