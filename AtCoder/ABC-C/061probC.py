from operator import itemgetter

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=itemgetter(0))

re = K
for a, b in AB:
    if re <= b:
        print(a)
        break
    re -= b