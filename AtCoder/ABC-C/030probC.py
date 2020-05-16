from bisect import bisect_left

N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


ans = 0
a = 0
while True:
    b = bisect_left(B, A[a]+X)
    if b >= M:
        break
    a = bisect_left(A, B[b]+Y)
    #print(a, b)
    ans += 1
    if a >= N:
        break

print(ans)