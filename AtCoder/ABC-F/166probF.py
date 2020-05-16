import sys
input = sys.stdin.readline


N, A, B, C = map(int, input().split())
Ss = [input().rstrip() for _ in range(N)]



ok = True
ans = []
for i, S in enumerate(Ss):
    if S == "AC":
        if A > C:
            T = "C"
            C += 1
            A -= 1
        elif A < C:
            T = "A"
            A += 1
            C -= 1
        elif i != N-1:
            if "A" in Ss[i+1]:
                T = "A"
                A += 1
                C -= 1
            else:
                T = "C"
                A -= 1
                C += 1
        else:
            T = "A"
            A += 1
            C -= 1
    elif S == "AB":
        if A > B:
            T = "B"
            B += 1
            A -= 1
        elif A < B:
            T = "A"
            A += 1
            B -= 1
        elif i != N-1:
            if "A" in Ss[i+1]:
                T = "A"
                A += 1
                B -= 1
            else:
                T = "B"
                A -= 1
                B += 1
        else:
            T = "A"
            A += 1
            B -= 1
    else:
        if B > C:
            T = "C"
            C += 1
            B -= 1
        elif B < C:
            T = "B"
            B += 1
            C -= 1
        elif i != N-1:
            if "B" in Ss[i+1]:
                T = "B"
                B += 1
                C -= 1
            else:
                T = "C"
                B -= 1
                C += 1
        else:
            T = "B"
            B += 1
            C -= 1
    if A < 0 or B < 0 or C < 0:
        ok = False
        break
    ans.append(T)

if ok:
    print("Yes")
    print("\n".join(ans))
else:
    print("No")