import sys
input = sys.stdin.readline

Q = int(input())
data = []
for _ in range(Q):
    S = input().rstrip()
    T = input().rstrip()
    data.append((S, T))

for S, T in data:
    j = 0
    i = 0
    ok = True
    if S[0] != T[0]:
        ok = False
    else:
        while j < len(S) and i < len(T):
            if S[j] == T[i]:
                j += 1
                i += 1
            elif S[j-1] == T[i]:
                i += 1
            else:
                ok = False
                break
        if j < len(S):
            ok = False
        if i < len(T):
            for j in range(i, len(T)):
                if S[-1] != T[j]:
                    ok = False
    if ok:
        print("YES")
    else:
        print("NO")