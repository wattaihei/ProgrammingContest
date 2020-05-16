N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort(reverse=True)
A = R[:K]
A = A[::-1]

ans = 0
for a in A:
    ans = (a+ans)/2

print(ans)