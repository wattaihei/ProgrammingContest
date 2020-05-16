N = int(input())
B = list(map(int, input().split()))

if N == 2:
    ans = 2*B[0]
else:
    ans = B[0]
    for i in range(N-2):
        ans += min(B[i], B[i+1])
    ans += B[-1]
print(ans)