N = int(input())
A = [a-i-1 for i, a in enumerate(list(map(int, input().split())))]

A.sort()

if N % 2 != 0:
    T = A[N//2]
else:
    T = (A[N//2-1] + A[N//2])//2

ans = 0
for a in A:
    ans += abs(a-T)
print(ans)