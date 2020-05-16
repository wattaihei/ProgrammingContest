T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ma = A[1]-1

    ans.append(min(ma, N-2))

for a in ans:
    print(a)
