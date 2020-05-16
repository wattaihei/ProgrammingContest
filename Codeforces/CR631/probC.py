import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

small = 0
large = 0
for i, a in enumerate(A):
    if a > N-i:
        small = 10**14
        break
    small = max(small, a+i)
    large += a


if small <= N <= large:
    blank = N-small
    ind = N-A[-1]+1
    ans = []
    for i in reversed(range(M-1)):
        ans.append(str(ind))
        a = A[i]
        slimit = i+1
        ind = max(ind-a, slimit)

    ans.append("1")
    
    print(" ".join(ans[::-1]))
else:
    print(-1)