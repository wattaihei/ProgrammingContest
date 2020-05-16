import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    S = ""
    for _ in range(9):
        a = input()
        S += a
    Query.append(S)

for S in Query:
    print(S.replace("1", "2"))