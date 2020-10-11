A = list(map(int, input().split()))
ans = 10**18
for i in range(len(A)-1):
    ans = min(ans, abs(A[i]-A[i+1]))
print(ans)