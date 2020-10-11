import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for d in range(1, N//2):
    tmp = 0
    checked = set()
    for t in range(N//d):
        ind = d*t
        if ind + d >= N-1 or ind in checked or ind == N - 1 - ind: break
        tmp += A[ind] + A[-ind-1]
        checked.add(N-1-ind)
        ans = max(ans, tmp)
print(ans)