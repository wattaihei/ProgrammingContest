S = list(input())
N = len(S)

Small = [chr(i) for i in range(97, 97+26)]
Big = [chr(i) for i in range(65, 65+26)]
Nums = [str(i) for i in range(10)]

def case(S):
    inds = 0
    while inds < N and S[inds] == "_":
        inds += 1
    if inds == N:
        return S
    inde = N-1
    while S[inde] == "_":
        inde -= 1

    isCamel = S[inds] in Small
    isUnderScore = S[inds] in Small
    for i in range(inds, inde+1):
        s = S[i]
        if s == "_":
            isCamel = False
            if i < inde and (not S[i+1] in Small):
                return S
        elif s in Big:
            isUnderScore = False
    if not isCamel and not isUnderScore:
        return S
    
    ans = ["_" for _ in range(inds)]
    if isCamel:
        for i in range(inds, inde+1):
            if S[i] in Big:
                ans.append("_")
                ans.append(S[i].lower())
            else:
                ans.append(S[i])
    else:
        mustup = False
        for i in range(inds, inde+1):
            s = S[i]
            if s == "_":
                mustup = True
            elif mustup:
                ans.append(s.upper())
                mustup = False
            else:
                ans.append(s)

    for _ in range(inde+1, N):
        ans.append("_")
    return ans


print("".join(case(S)))