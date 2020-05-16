a, b, c, d = map(int, input().split())
A = [a, b, c]
A.sort()
ans = max(d-A[1]+A[0], 0) + max(d-A[2]+A[1], 0)
print(ans)