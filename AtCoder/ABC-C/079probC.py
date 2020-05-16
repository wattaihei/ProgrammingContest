S = [int(a) for a in list(input())]

num = []
def make(B):
    if len(B) == 3:
        num.append(B)
        return
    B1 = B[:]
    B2 = B[:]
    B1.append(1)
    B2.append(-1)
    make(B1)
    make(B2)

make([])

for A in num:
    k = S[0] + S[1]*A[0] + S[2]*A[1] + S[3]*A[2]
    if k == 7:
        break

ans = []
for a in A:
    if a == 1:
        ans.append('+')
    else:
        ans.append('-')

print(str(S[0])+ans[0]+str(S[1])+ans[1]+str(S[2])+ans[2]+str(S[3])+'=7')