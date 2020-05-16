N, M = map(int, input().split())

# 2(N+x) = M-2x
# x = (M-2N)/4
if M < 2*N:
    ans = M//2
else:
    x = (M-2*N)//4
    ans = N + x
print(ans)