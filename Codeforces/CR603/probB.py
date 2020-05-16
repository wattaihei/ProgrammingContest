import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    Ss = [input().rstrip() for _ in range(N)]
    Query.append((N, Ss))

for N, Ss in Query:
    mustchange = [False]*N
    already = set()
    c = 0
    for i, S in enumerate(Ss):
        if S in already:
            c += 1
            mustchange[i] = True
        else:
            already.add(S)
    
    ans = []
    for i, S in enumerate(Ss):
        if mustchange[i]:
            for n in range(10):
                T = str(n) + S[1:]
                if not T in already:
                    ans.append(T)
                    already.add(T)
                    break
                R = S[:3] + str(n)
                if not R in already:
                    ans.append(R)
                    already.add(R)
                    break               
        else:
            ans.append(S)
    print(c)
    print("\n".join(ans))