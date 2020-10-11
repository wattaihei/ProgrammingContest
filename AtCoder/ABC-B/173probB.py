from collections import Counter

N = int(input())
Ss = [input() for _ in range(N)]

C = Counter(Ss)
for s in ["AC", "WA", "TLE", "RE"]:
    if not s in C:
        c = 0
    else:
        c = C[s]
    print("{} x {}".format(s, c))