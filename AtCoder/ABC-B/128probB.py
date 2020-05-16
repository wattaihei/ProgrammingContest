N = int(input())
SP = []
for i in range(1, N+1):
    Si, Pi = map(str, input().split())
    SP.append([Si, int(Pi), i])

SP = sorted(SP, key=lambda x: x[1], reverse=True)
SP = sorted(SP, key=lambda x: x[0])
for sp in SP:
    print(sp[2])
