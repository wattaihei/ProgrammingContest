# 最長共通接頭辞問題(Z-Algorithm)
# 文字列SとS[i:]の最長共通接頭辞を各iについて求める
# 参考：https://codeforces.com/blog/entry/3107
# 図がわかりやすい:https://snuke.hatenablog.com/entry/2014/12/03/214243

N = int(input())
S = list(input())

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
print(Z)