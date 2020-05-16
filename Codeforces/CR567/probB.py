import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

L = [[] for _ in range(N)]
for n in range(N-1):
    if S[n+1] != '0':
        L[max(n+1, N-n-1)].append(n)

def make_sum(s1, s2):
    if len(s1) < len(s2):
        tmp = s2
        s2 = s1
        s1 = tmp
    l1, l2 = len(s1), len(s2)
    s2 = '0'*(l1-l2) + s2

    S = [0]*(l1+1)
    for i in range(l1):
        a = int(s2[-i-1]) + int(s1[-i-1]) + S[i]
        S[i] = a%10
        S[i+1] += a//10
    
    go = False
    a = ''
    for n in range(l1, -1, -1):
        if S[n] == 0 and not go:
            continue
        else:
            go = True
            a += str(S[n])

    return a


def smaller(s1, s2):
    if len(s1) > len(s2):
        return s2
    elif len(s1) < len(s2):
        return s1
    else:
        l = len(s1)
        for i in range(l):
            if s1[i] > s2[i]:
                return s2
            elif s1[i] < s2[i]:
                return s1
    return s1

ans = '9'*N
c = 0
for l in range(N):
    update = False
    for n in L[l]:
        s1, s2 = S[:n+1], S[n+1:]
        a = make_sum(s1, s2)
        ans = smaller(ans, a)
        update = True
    if update:
        c += 1
    if c > 3:
        break

print(ans)
