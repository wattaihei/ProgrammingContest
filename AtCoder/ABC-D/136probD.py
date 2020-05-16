import sys
input = sys.stdin.readline
S = list(input())
S.pop()

l = 0
r = 0
ans = [0 for _ in range(len(S))]
for i, s in enumerate(S):
    #print(i, ans)
    if s == 'R':
        if i % 2 == 0:
            l += 1
        else:
            r += 1
    else:
        if S[i-1] == 'R':
            k = i
            if i % 2 == 0:
                ans[i-1] += r
                ans[i] += l+1
            else:
                ans[i-1] += l
                ans[i] += r+1
            l = 0
            r = 0
        else:
            if (i-k)%2 == 0:
                ans[k] += 1
            else:
                ans[k-1] += 1
print(' '.join([str(a) for a in ans]))