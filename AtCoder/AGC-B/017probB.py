N, A, B, C, D = map(int, input().split())

ans = 'NO'
for n in range(N+1):
    if A + n*C - (N-1-n)*D <= B <= A + n*D - (N-1-n)*C:
        ans = 'YES'
        break
print(ans)