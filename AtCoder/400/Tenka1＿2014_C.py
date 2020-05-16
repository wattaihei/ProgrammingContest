import sys
input = sys.stdin.readline

def convert(S):
    h, m = S.split(":")
    return int(h)*60+int(m)

N = int(input())
# AB = []
# for _ in range(N):
#     sA, sB = input().rstrip().split()
#     a, b = convert(sA), convert(sB)
#     AB.append((a, b))

P = []
def dfs(dmax, now):
    if len(now) == N:
        P.append(now)
        return 
    for n in range(dmax+2):
        dfs(max(n, dmax), now+[n])
    
dfs(-1, [])
# print(P)