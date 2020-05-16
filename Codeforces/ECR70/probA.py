import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input().rstrip())
    T = list(input().rstrip())
    Query.append((S, T))

for S, T in Query:
    L = len(T)
    L2 = len(S)
    for i in range(L):
        if T[-i-1] == "1":
            for j in range(i, L2):
                if S[-j-1] == "1":
                    ans = j-i
                    break
            break
    print(ans)