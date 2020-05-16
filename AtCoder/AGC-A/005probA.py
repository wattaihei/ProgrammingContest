X = input()
N = len(X)

c = 0
uppun = 0
for i, x in enumerate(X):
    if x == 'S':
        uppun += 1
    if x == 'T':
        c += 1
        if uppun > 0:
            uppun -= 1
    if c == N//2:
        ans = N - (i+1-c - uppun)*2
        break

print(ans)