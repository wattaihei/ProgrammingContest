

N = int(input())

def inverse(P):
    ret = []
    for p in P:
        ret.append(p^1)
    return ret

def solve(N):
    if N == 1:
        return [[0, 1]]
    Pre = solve(N-1)
    ret = []
    ret.append([0]*(2**(N-1)) + [1]*(2**(N-1)))
    for P in Pre:
        ret.append(P+P)
        ret.append(P+inverse(P))
    return ret

AB = "AB"
ans = solve(N)
print(len(ans))
for P in ans:
    for i in P:
        print(AB[i], end="")
    print()