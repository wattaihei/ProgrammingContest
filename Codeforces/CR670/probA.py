import sys
input = sys.stdin.buffer.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*101
    for a in A:
        B[a] += 1
    
    a1 = 0
    u1 = False
    u2 = False
    a2 = 0
    for n, b in enumerate(B):
        if b >= 2 and not u1:
            a1 = n+1
        else:
            u1 = True
        if b >= 1 and not u2:
            a2 = n+1
        else:
            u2 = True
    
    print(a1+a2)
