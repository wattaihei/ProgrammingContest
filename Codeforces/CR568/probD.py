from operator import itemgetter
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    B = list(map(int, input().split()))

    A = []
    for i, b in enumerate(B):
        A.append((i+1, b))

    A.sort(key=itemgetter(1))

    a0, a1 = A[0][1], A[1][1]
    A1 = [a0+(a1-a0)*j for j in range(N-1)]
    dif = []
    i = 0
    j = 0
    ok = True
    while i < N and j < N-1:
        if A[i][1] == A1[j]:
            i += 1
            j += 1
        elif i < N-1:
            if A[i+1][1] == A1[j]:
                dif.append(A[i][0])
                i += 1
            else:
                ok = False
                break
        else:
            ok = False
            break
        if i != j and i != j+1:
            ok = False
            break
    if ok:
        if len(dif) == 1:
            print(dif[0])
            return
        elif len(dif) == 0:
            print(A[N-1][0])
            return
    
    a1, a2 = A[1][1], A[2][1]
    A2 = [a1+(a2-a1)*(j-1) for j in range(N)]
    ok = True
    for i in range(1, N):
        if A[i][1] != A2[i]:
            ok = False
            break
    if ok:
        print(A[0][0])
        return
    
    ok = True
    d = (a2-a0)
    A3 = [a0+d*j for j in range(N-1)]
    for j in range(1, N-1):
        if A[j+1][1] != A3[j]:
            ok = False
            break
    if ok:
        print(A[1][0])
        return
    
    print(-1)


if __name__ == "__main__":
    main()