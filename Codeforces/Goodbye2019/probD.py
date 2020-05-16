import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def inout(A):
    print("?", end=" ")
    print(*A)
    sys.stdout.flush()

    pos, a = map(int, input().split())
    return pos, a

dic = {}
for k in range(1, K+2):
    A = list(range(1,k)) + list(range(k+1, K+2))
    pos, a = inout(A)
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

S =  list(dic.items())
S.sort()
ind = S[1][1]

print("!", ind)