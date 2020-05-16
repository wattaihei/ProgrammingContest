import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Query.append((N, A, B))

for N, A, B in Query:
    ok = True
    dif = 0
    for i in range(N):
        if A[i] != B[i]:
            if dif == 0:
                d = A[i] - B[i]
                if d > 0:
                    ok = False
                dif += 1
            elif dif == 1:
                if A[i] - B[i] != d:
                    ok = False
            else:
                ok = False
        else:
            if dif == 0:
                continue
            elif dif == 1:
                dif += 1
    print("YES" if ok else "NO")