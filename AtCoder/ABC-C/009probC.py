N, K = map(int, input().split())
S = list(input())

A = sorted(S, reverse=True)

def search(k, remain, ans):
    l = len(ans)
    to_compare = sorted(S[l+1:])
    for r in remain:
        