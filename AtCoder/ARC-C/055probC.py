def Z_Algorithm(S):
    N = len(S)
    R = 0 # Rはi文字目まで読んだ時、接頭辞の右端のうち一番右側にくるようなもの
    L = 0 # Lはその範囲の左端
    Z = [0 for _ in range(N)] # 答えとなる最長接頭辞の長さ
    Z[0] = N

    for i in range(1, N):
        if i > R:
            # iが前のRより右側ならS[i:]とSのみで考える
            L = i
            R = i
            while (R < N and S[R-L] == S[R]):
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                # はみ出さないなら前のがそのまま使える。R,Lはそのまま
                Z[i] = Z[k]
            else:
                # はみ出したら伸ばしてく
                L = i
                while (R < N and S[R-L] == S[R]):
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
Z1 = Z_Algorithm(S)[1:]
Z2 = Z_Algorithm(S[::-1])[-1:0:-1]

ans = 0
for l, (z1, z2) in enumerate(zip(Z1, Z2)):
    z2 = min(z2, N-l-2)
    if l < N//2 or z1 <= 0 or z2 <= 0: continue
    ans += min([max(z1+z2-(N-l-2), 0), N-l-2, z1, z2])
print(ans)