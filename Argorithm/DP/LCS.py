# 最長共通部分列問題
# AOJ DP ALDS1_10_C より

Q = int(input())
AB = []
for _ in range(Q):
    A = list(input())
    B = list(input())
    AB.append([A, B])

for A, B in AB:
    a = len(A)
    b = len(B)
    # Aの0からi, Bの0からjまでの文字で共通しているものの個数
    dp = [[0 for _ in range(b)] for _ in range(a)]

    # テーブルの上と左、初期値設定
    for i in range(a):
        if A[i] == B[0]:
            dp[i][0] = 1
    for j in range(b):
        if A[0] == B[j]:
            dp[0][j] = 1
    
    for i in range(1, a):
        for j in range(1, b):
            if A[i] == B[j]:
                # もし次につなげるのが一緒ならそれをつなげるだけ
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # AかBの直前のやつのうちいい方
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    #for d in dp:
    #    print(d)
    print(dp[a-1][b-1])