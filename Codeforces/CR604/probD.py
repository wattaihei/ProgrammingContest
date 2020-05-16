import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().split())
if A+C == B+D:
    if B >= A and C >= D:
        print("YES")
        ans = []
        for _ in range(D):
            ans.append(3)
            ans.append(2)
        for _ in range(C-D):
            ans.append(1)
            ans.append(2)
        for _ in range(A):
            ans.append(1)
            ans.append(0)
        print(" ".join([str(a) for a in ans]))
    else:
        print("NO")
elif A+C == B+D+1:
    if B >= A and C >= D+1:
        print("YES")
        ans = []
        for _ in range(A):
            ans.append(0)
            ans.append(1)
        for _ in range(B-A):
            ans.append(2)
            ans.append(1)
        for _ in range(D):
            ans.append(2)
            ans.append(3)
        ans.append(2)
        print(" ".join([str(a) for a in ans]))
    elif A == B+1 and C == 0 and D == 0:
        print("YES")
        ans = []
        for _ in range(B):
            ans.append(0)
            ans.append(1)
        ans.append(0)
        print(" ".join([str(a) for a in ans]))   
    else:
        print("NO")
elif B+D == A+C+1:
    if B >= A+1 and C >= D:
        print("YES")
        ans = []
        for _ in range(D):
            ans.append(3)
            ans.append(2)
        for _ in range(C-D):
            ans.append(1)
            ans.append(2)
        for _ in range(A):
            ans.append(1)
            ans.append(0)
        ans.append(1)
        print(" ".join([str(a) for a in ans]))
    elif D == C+1 and A == 0 and B == 0:
        print("YES")
        ans = []
        for _ in range(C):
            ans.append(3)
            ans.append(2)
        ans.append(3)
        print(" ".join([str(a) for a in ans]))          
    else:
        print("NO")
else:
    print("NO")        