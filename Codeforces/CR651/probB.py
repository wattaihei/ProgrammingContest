import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    E = []
    O = []
    for i, a in enumerate(A):
        if a%2 == 0:
            E.append(i+1)
        else:
            O.append(i+1)
    
    if len(E)%2 == 1:
        E.pop()
        O.pop()
    elif E:
        E.pop()
        E.pop()
    else:
        O.pop()
        O.pop()
    
    for i in range(len(E)//2):
        print(E[2*i], E[2*i+1])
    for i in range(len(O)//2):
        print(O[2*i], O[2*i+1])