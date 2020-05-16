N = int(input())
A = list(map(int, input().split()))


B = []
checked = [0 for _ in range(N)]
for i in range(N, 0, -1):
    num = N // i
    a = A[i-1]
    for j in range(1, num+1):
        a += checked[j*i-1]
    if a % 2 == 1:
        B.append(i)
        checked[i-1] = 1
print(len(B))
print(' '.join([str(b) for b in B]))