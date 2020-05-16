import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
T = input().rstrip()


def other(P):
    for s in ["a", "b", "c"]:
        if not s in P:
            return s

if S[0] == S[1]:
    if S == T:
        tmp = S[0]
        for a in ["a", "b", "c"]:
            if not a in S:
                tmp += a
        ans = tmp*N
    elif T[0] == S[0]:
        ans = (S[0]+other(S+T)+T[1])*N
    elif T[1] == S[0]:
        ans = (S[0] + T[0] + other(S+T))*N
    else:
        ans = (S[0] + T[1] + other(S+T[1]))*N
elif T[0] == T[1]:
    if S[0] == T[0]:
        ans = (T[0]+other(S+T)+S[1])*N
    elif S[1] == T[0]:
        ans = (T[0] + S[0] + other(S+T))*N
    else:
        ans = (T[0] + S[1] + other(T+S[1]))*N
else:
    if S[0] == T[0]:
        ans = S[1]*N + other(S)*N + S[0]*N
    elif S[1] == T[1]:
        ans = S[1]*N + S[0]*N + T[0]*N
    elif S[0] == T[1]:
        ans = S[0]*N + other(S)*N + S[1]*N
    else:
        ans = T[0]*N + other(T)*N + T[1]*N

print("YES")
print(ans)