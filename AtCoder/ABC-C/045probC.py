S = input()
N = len(S)

def num(k, s, ans):
    # 長さk
    if k == N:
        for a in s:
            ans += int(a)
        return ans
    ss = s[:]
    sss = s[:]
    l = ss.pop()
    ss.append(l+S[k])
    sss.append(S[k])
    ans1 = num(k+1, ss, ans)
    ans2 = num(k+1, sss, ans1)
    return ans2

print(num(1, [S[0]], 0))