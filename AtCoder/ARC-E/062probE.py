import sys
input = sys.stdin.buffer.readline


N = int(input())
Ps = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

def rotations(P):
    p0, p1, p2, p3 = P
    return [P, (p1, p2, p3, p0), (p2, p3, p0, p1), (p3, p0, p1, p2)]

def inout(P):
    p0, p1, p2, p3 = P
    return (p3, p2, p1, p0)

def similarity(P):
    p0, p1, p2, p3 = P
    if p0 == p2 and p1 == p3:
        if p0 == p1:
            return 4
        return 2
    return 1

dic = {}
for P in Ps:
    isNew = True
    for R in rotations(P):
        if R in dic:
            dic[R] += 1
            isNew = False
            break
    if isNew:
        dic[P] = 1

ans = 0
for i, P1 in enumerate(Ps):
    p10, p11, p12, p13 = P1
    for j in range(i):
        for P2 in rotations(Ps[j]):
            p20, p21, p22, p23 = inout(P2)
            lefts = [
                (p11, p10, p20, p21),
                (p12, p11, p21, p22),
                (p13, p12, p22, p23),
                (p10, p13, p23, p20)
                ]
            
            dic2 = {}
            for L in lefts:
                registered = False
                for Lr in rotations(L):
                    if Lr in dic:
                        dic2[Lr] = dic2.get(Lr, 0) + 1
                        registered = True
                        break
                if not registered:
                    dic2 = {}
                    break
            if not dic2: continue

            count = 1
            for P, c in dic2.items():
                s = similarity(P)
                c2 = dic[P]
                if P in rotations(P1): c2 -= 1
                if P in rotations(P2): c2 -= 1
                # t = 1
                for d in range(c):
                    count *= (c2-d)*s
                # count += t
            
            # count //= min(similarity(P1), similarity(P2))
            ans += count

ans //= 3
print(ans)
