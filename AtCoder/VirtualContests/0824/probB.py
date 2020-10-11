A, B, K = map(int, input().split())
if K <= A:
    ans = (A - K, B)
elif K <= A+B:
    ans = (0, A+B-K)
else:
    ans = (0, 0)
print(*ans)