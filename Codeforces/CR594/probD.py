import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

Ls = []
Rs = []
for i in range(N):
    if S[i] == "(":
        Ls.append(i)
    else:
        Rs.append(i)

if len(Ls) != len(Rs):
    print(0)
    print(1, 1)
else:
    ans = -1
    al, ar = 0, 0
    for l in Ls:
        for r in Rs:
            P = S[:]
            P[l] = S[r]
            P[r] = S[l]
            a = 0
            A = []
            for i in range(N):
                if P[i] == "(":
                    a += 1
                else:
                    a -= 1
                A.append(a)
            b = min(A)
            s = 0
            for a in A:
                if b - a >= 0:
                    s += 1
            if ans < s:
                ans = s
                al, ar = l+1, r+1
    print(ans)
    print(al, ar)
