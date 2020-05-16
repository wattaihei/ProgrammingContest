import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input().rstrip())
    Query.append(S)

for S in Query:
    L = len(S)
    A1 = []
    A2 = []
    for s in S:
        a = int(s)
        if a % 2 == 0:
            A1.append(a)
        else:
            A2.append(a)
    A1 = A1[::-1]
    A2 = A2[::-1]
    ans = []
    while A1 or A2:
        if not A1:
            a = A2.pop()
        elif not A2:
            a = A1.pop()
        elif A1[-1] < A2[-1]:
            a = A1.pop()
        else:
            a = A2.pop()
        ans.append(a)
    print(''.join([str(a) for a in ans]))