import sys
input = sys.stdin.readline

Q = int(input())
Query = [input().rstrip() for _ in range(Q)]

for S in Query:
    L = len(S)
    if L < 3:
        print(0)
        print()
    else:
        A = []
        for i in range(1, L-1):
            if S[i-1:i+2] == "one":
                A.append((i, 1))
            elif S[i-1:i+2] == "two":
                A.append((i, 2))
        if len(A) == 0:
            print(0)
            print()
        else:
            ans = []
            skip = False
            for j in range(len(A)-1):
                if skip:
                    skip = False
                elif A[j+1][0] - A[j][0] == 2 and A[j+1][1] == 1 and A[j][1] == 2:
                    skip = True
                    ans.append(A[j][0]+1)
                else:
                    ans.append(A[j][0])
            if not skip:
                ans.append(A[-1][0])
            
            print(len(ans))
            print(" ".join([str(a+1) for a in ans]))
