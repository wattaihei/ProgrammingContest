N = int(input())
A = list(map(int, input().split()))

ans = 0

l = 0
r = 0
s = 0
while l <= N-1 and r <= N-1:
    if s + A[r] == s ^ A[r]:
        s += A[r]
        ans += r-l+1
        r += 1
    else:
        s -= A[l]
        l += 1
            

print(ans)