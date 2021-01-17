import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

B = A + A

C = [0]
for b in B:
    C.append(C[-1]+b)

ans = 10**18
j = 0
for i in range(N):
    while j+1 <= i+N and C[j+1] - C[i] < C[i+N] - C[j+1]:
        j += 1
    ans = min(ans, abs(2*C[j]-C[i]-C[i+N]))
    ans = min(ans, abs(2*C[j+1]-C[i]-C[i+N]))

print(ans)