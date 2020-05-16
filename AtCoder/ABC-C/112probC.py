from operator import itemgetter

N = int(input())
xyh = [list(map(int, input().split())) for _ in range(N)]
checked = [[False for _ in range(101)] for _ in range(101)]

xyh.sort(key=itemgetter(2), reverse=True)

q = [xyh[0]]
ans = []
c = 0
while not ans:
    qq = []
    for s in q:
        x = s[0]
        y = s[1]
        for i, d in enumerate(xyh):
            print(s, d)
            if d[2] == 0:
                continue
            ch = abs(d[0] - x) + abs(d[1] - y) + d[2]
            if i == 0:
                chpre = ch
            if chpre != ch:
                break
        if chpre == ch:
            ans = [x, y, ch]
            break
        checked[x][y] = True
        nexts = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        for ne in nexts:
            nx = ne[0]
            ny = ne[1]
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                if not checked[nx][ny]:
                    qq.append(ne)
    q = qq

print(' '.join([str(a) for a in ans]))
        
        

