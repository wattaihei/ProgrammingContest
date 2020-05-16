import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

def check(N, A):
    for i in range(N-1):
        a, b = A[i], A[i+1]
        if b != a+1 and b > a:
            return False
    return True

for N, A in Query:
    print("Yes" if check(N, A) else "No")