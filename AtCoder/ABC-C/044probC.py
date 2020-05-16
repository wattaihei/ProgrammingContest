from collections import Counter

N, K = map(int, input().split())
A = list(map(lambda x:int(x)-K, input().split()))

def Sum_list(i, s, L, ans):
    if i == len(L):
        ans.append(s)
        return ans
    ans = Sum_list(i+1, s, L, ans)
    ans = Sum_list(i+1, s+L[i], L, ans)
    return ans

def main():
    M = []
    P = []
    zero = 0
    for a in A:
        if a < 0:
            M.append(a)
        elif a > 0:
            P.append(a)
        else:
            zero += 1

    SM = Sum_list(0, 0, M, [])
    CM = Counter(SM)
    SP = Sum_list(0, 0, P, [])
    CP = Counter(SP)

    ans = 0
    for k, v in CP.items():
        if k == 0:
            continue
        if -k in CM.keys():
            ans += CM[-k]*v

    print(ans*2**zero+2**zero-1)

if __name__ == "__main__":
    main()