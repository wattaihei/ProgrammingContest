import sys
input = sys.stdin.readline

mod = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))

Mi = []
for a in A:
    if a != 0:
        Mi.append((abs(a), a//abs(a)))

Mi.sort(reverse=True)

if len(Mi) < K:
    ans = 0
else:
    ans = 1
    seg = 1
    lastinv = -1
    lastpu = -1
    for i in range(K):
        a, iv = Mi[i]
        seg *= iv
        if iv == -1:
            lastinv = a
        else:
            lastpu = a
        ans = ans * a % mod

    if seg == -1:
        fpu = -1
        fmi = -1
        ind = K
        while ind < len(Mi):
            a, iv = Mi[ind]
            ind += 1
            if iv == -1:
                if fmi == -1:
                    fmi = a
            else:
                if fpu == -1:
                    fpu = a
        
        if lastpu == -1:
            if fpu != -1:
                ans = ans * fpu * pow(lastinv, mod-2, mod) % mod
            elif 0 in A:
                ans = 0
            else:
                ans = -1
                for i in range(K):
                    ans = ans * Mi[-i-1][0] % mod
        elif fpu == -1 or fmi == -1:
            if fpu == -1 and fmi == -1:
                if 0 in A:
                    ans = 0
                else:
                    ans = -ans
            elif fpu == -1:
                ans = ans * fmi * pow(lastpu, mod-2, mod) % mod
            else:
                ans = ans * fpu * pow(lastinv, mod-2, mod) % mod
        elif lastpu * fpu > lastinv * fmi:
            ans = ans * fpu * pow(lastinv, mod-2, mod) % mod
        else:
            ans = ans * fmi * pow(lastpu, mod-2, mod) % mod
    
print(ans % mod)
            