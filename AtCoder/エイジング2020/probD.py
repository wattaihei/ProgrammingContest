import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

num = S.count('1')

n1 = num + 1
n2 = num - 1

def count(m):
    ret = 1
    while m != 0:
        k = bin(m).count("1")
        m %= k
        ret += 1
    return ret


if n2 != 0:
    start1 = 0
    start2 = 0
    pow1 = [1]
    pow2 = [1]
    for i in range(N):
        s = int(S[-1-i])
        start1 = (start1 + pow1[-1] * s) % n1
        start2 = (start2 + pow2[-1] * s) % n2
        pow1.append(pow1[-1] * 2 % n1)
        pow2.append(pow2[-1] * 2 % n2)


    ans = []
    for i in range(N):
        s = int(S[i])
        if s == 0:
            l = (start1 + pow1[-i-2]) % n1
            ans.append(count(l))
        else:
            l = (start2 - pow2[-i-2]) % n2
            ans.append(count(l))

    print(*ans, sep="\n")
else:
    start1 = 0
    pow1 = [1]
    for i in range(N):
        s = int(S[-1-i])
        start1 = (start1 + pow1[-1] * s) % n1
        pow1.append(pow1[-1] * 2 % n1)

        


    ans = []
    for i in range(N):
        s = int(S[i])
        if s == 0:
            l = (start1 + pow1[-i-2]) % n1
            ans.append(count(l))
        else:
            ans.append(0)

    print(*ans, sep="\n")