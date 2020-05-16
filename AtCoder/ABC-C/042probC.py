N, K = map(int, input().split())
D = list(map(int, input().split()))
n = len(str(N))

C = []
for k in range(10):
    if not k in D:
        C.append(k)

# 桁上がりを考えてなかった
def num(a):
    if len(a) == n:
        if int(a) >= N:
            return a
        return False
    for c in C:
        d = num(a + str(c))
        if not d is False:
            break
    return d

print(num(''))