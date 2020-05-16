import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    S = input().rstrip()
    Query.append(S)

for S in Query:
    is1 = "1" in S
    is0 = "0" in S
    if not is1 or not is0:
        print(S)
    else:
        T = ""
        for s in S:
            if T and T[-1] == s:
                T += str(int(s)^1)
            T += s
        print(T)