class SquareCityWalking():
    def largestGCD(self, N, A):
        ans = 1
        for a in range(1, 101):
            cango = [[False]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if A[i*N+j] % a == 0:
                        cango[i][j] = True
            if not cango[0][0] or not cango[N-1][N-1]:
                continue
            checked = [[False]*N for _ in range(N)]
            q = [(0, 0)]
            checked[0][0] = True
            while q:
                qq = []
                for x, y in q:
                    if x < N-1 and cango[x+1][y] and not checked[x+1][y]:
                        checked[x+1][y] = True
                        qq.append((x+1, y))
                    if y < N-1 and cango[x][y+1] and not checked[x][y+1]:
                        checked[x][y+1] = True
                        qq.append((x, y+1))
                q = qq
            if checked[N-1][N-1]:
                ans = a
        return ans