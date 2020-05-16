import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ok = True
checked = [0]*(10**6+1)
ans = []
ind = 0
used = set()
c = 0
for i, a in enumerate(A):
    if a > 0:
        if checked[a] == 0:
            if a in used:
                ok = False
                break
            checked[a] = 1
            c += 1
        else:
            ok = False
            break
    else:
        if checked[-a] == 1:
            used.add(-a)
            checked[-a] = 0
            c -= 1
        else:
            ok = False
            break
    if c == 0:
        ans.append(i+1-ind)
        ind = i+1
        used = set()

if not ok or c != 0:
    print(-1)
else:
    print(len(ans))
    print(" ".join([str(a) for a in ans]))