import sys
input = sys.stdin.readline

from bisect import bisect_left
from operator import itemgetter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = sorted(A)
    D = sorted(B)
    for i in range(N):
        if C[i] > D[i]:
            print('No')
            return

    for ind, a in enumerate(C):
        i = bisect_left(D, a)
        if ind != i:
            print('Yes')
            return
    E = [(C[0], D[N-1])]
    for i in range(N-1):
        E.append((C[i+1], D[i]))
    
    E.sort(key=itemgetter(1))
    E.sort(key=itemgetter(0))

    F = []
    for i in range(N):
        F.append((A[i], B[i]))
    F.sort(key=itemgetter(1))
    F.sort(key=itemgetter(0))
    
    for i in range(N):
        if F[i] != E[i]:
            print('Yes')
            return 
    
    print('No')
    return 

if __name__ == "__main__":
    main()