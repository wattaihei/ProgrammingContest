import sys
input = sys.stdin.readline

K = int(input())

def dfs(le, L, ret):
    if len(L) == le:
        ret.append(L)
        return ret
    l = L[-1]
    for num in range(max(0, l-1), min(l+1, 9)+1):
        ret = dfs(le, L+[num], ret)
    return ret

le = 0
ans = []
while True:
    le += 1
    for n in range(1, 10):
        ret = dfs(le, [n], [])
        if len(ret) < K:
            K -= len(ret)
        else:
            ans = ret[K-1]
            break
    if ans: break

print("".join([str(a) for a in ans]))