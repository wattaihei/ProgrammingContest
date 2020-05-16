K, A, B = map(int, input().split())

if B-A <= 2 or 1+K <= A:
    print(1+K)
else:
    remain_c = K + 1 - A
    ans = A + (remain_c//2) * (B-A) + remain_c%2
    print(ans)