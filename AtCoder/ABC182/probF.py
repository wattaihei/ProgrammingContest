import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

dic = {}

def solve(x, ind):
    if (x, ind) in dic:
        return dic[(x, ind)]
    if x == 0 or ind == 0:
        return 1
    ret = 0
    a = A[ind]
    ret += solve(x%a, ind-1)
    if x%a != 0 and (ind==N-1 or (x//a+1)*a != A[ind+1]):
        ret += solve((x//a+1)*a - x, ind-1)
    dic[(x, ind)] = ret
    # print(x, ind, ret)
    return ret

if N == 1:
    ans = 1
else:
    ans = solve(X, N-1)
print(ans)