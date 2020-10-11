class StarsInTheSky():
    def countPictures(self, N, Xs, Ys):
        INF = 10**18
        ans = 0
        for bit in range(1<<N):
            ok = True
            dpx = [INF, -INF]
            dpy = [INF, -INF]
            for i, (x, y) in enumerate(zip(Xs, Ys)):
                if bit&(1<<i):
                    dpx[0] = min(dpx[0], x)
                    dpx[1] = max(dpx[1], x)
                    dpy[0] = min(dpy[0], y)
                    dpy[1] = max(dpy[1], y)
            for i, (x, y) in enumerate(zip(Xs, Ys)):
                if not bit&(1<<i):
                    if dpx[0] <= x <= dpx[1] and dpy[0] <= y <= dpy[1]:
                        ok = False
                        break
            if ok:
                ans += 1
        return ans-1

# {6, 9, 4, 4, 6, 6, 4, 6, 2}