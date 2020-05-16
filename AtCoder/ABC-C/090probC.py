N, M = map(int, input().split())

if N >= 2 and M >= 2:
    ans = (N-2)*(M-2)
elif N == 1 and M >= 2:
    ans = M-2
elif N >= 2 and M == 1:
    ans = N-2
else:
    ans = 1

print(ans)