import sys
input = sys.stdin.readline
from collections import Counter

mod = 10**9+7

def power_func(a,n,mod=mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if A[0] != 0:
        print(0)
        return
    C = Counter(A)
    if C[0] > 1:
        print(0)
        return

    ans = 1
    B = sorted(C.items())
    for i in range(len(B)-1):
        a1, n1 = B[i]
        a2, n2 = B[i+1]
        if a2 != a1 + 1:
            print(0)
            return
        c = power_func(2, n1) - 1
        if c <= 0: c += mod
        ans = ans * power_func(c, n2) % mod
        ans = ans * power_func(2, n2*(n2-1)//2) % mod
    
    print(ans)
    return
    


if __name__ == "__main__":
    main()