A = list(map(int, input().split())) # 横に2個

A.sort()

ans = 0
pre = A[0]
for a in A:
    ans += a - pre
    pre = a

print(ans)