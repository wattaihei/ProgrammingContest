import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(input().rstrip())

Query = []
NUM = 0
while True:
    T = []
    for i in range(N-1):
        if S[i] == "R" and S[i+1] == "L":
            T.append(str(i+1))
    if not T:
        break
    for t in T:
        S[int(t)-1] = "L"
        S[int(t)] = "R"
    NUM += len(T)
    Query.append(T)


if len(Query) <= K <= NUM:
    delta = K - len(Query)
    ans = [None]*K
    ind = 0
    for T in Query:
        if len(T)-1 <= delta:
            for t in T:
                ans[ind] = ["1", t]
                ind += 1
            delta -= len(T) - 1
        elif delta > 0:
            for i, t in enumerate(T):
                if delta > 0:
                    ans[ind] = ["1", t]
                    ind += 1
                    delta -= 1
                else:
                    ans[ind] = [str(len(T)-i)] + T[i:]
                    ind += 1
                    break
        else:
            ans[ind] = [str(len(T))] + T
            ind += 1
    #for A in ans:
    #    print(*map(str, A))
    print("\n".join([" ".join(A) for A in ans]))
else:
    print(-1) 