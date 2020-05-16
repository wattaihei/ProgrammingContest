H, W, A, B = map(int, input().split())

T = [[0 for _ in range(B+1)] for _ in range(A+1)]
for a in range(A-1, -1, -1):
    for b in range(B-1, -1, -1):
        T[a][b] = T[a+1][b] + T[a][b+1] + a*b

KA = [0 for _ in range(A+1)] 
for a in range(A-1, -1, -1):
    KA[a] = KA[a+1] + B*a

KB = [0 for _ in  range(B+1)]
for b in range(B-1, -1, -1):
    KB[b] = KB[b+1] + A*b

S = 0
for h in range(H-A+1):
    for w in range(W-B+1):
        upA = max(A-h, 0)
        upB = max(B-w, 0)
        doA = max(H-A-(h+A), 0)
        doB = max(W-B-(w+B), 0)
        S += T[upA][upB] + T[doA][upB] + T[upA][doB] + T[doA][doB]
        S += KA[upA] + KA[doA] + KB[upB] + KB[doB]
        S += A*B
        print(S)

ans = S / (H-A+1)**2 / (W-B+1)**2
print(ans)