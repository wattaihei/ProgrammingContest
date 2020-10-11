import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a, b, c = sorted([A[i], A[j], A[k]])
            if a != b and b != c and c < a + b:
                ans += 1
print(ans)