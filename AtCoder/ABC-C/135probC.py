N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pre = 0
ans = 0
for i, a in enumerate(A):
    if i == N:
        ans += min(pre, a)
        break
    if a <= pre:
        ans += a
        pre = B[i]
    elif pre < a < pre + B[i]:
        ans += a
        pre = B[i]+pre - a
    else:
        ans += pre + B[i]
        pre = 0

print(ans)