import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(a) for a in list(input().rstrip())]

B = A[:K]
ok = True
for i in range(N):
    if A[i] < B[i%K]:
        ok = True
        break
    elif A[i] > B[i%K]:
        ok = False
        break


if not ok:
    ind = K-1
    while True:
        B[ind] += 1
        if B[ind] == 10:
            B[ind] = 0
            ind -= 1
        else:
            break

ans = []
for i in range(N):
    ans.append(B[i%K])
print(N)
print(*ans, sep="")