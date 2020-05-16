import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, list(input().rstrip())))


def contains(n):
    t = n&-n
    return t.bit_length()


def solve1(A, D):
    is1 = False
    cmb_e = 0
    for i, a in enumerate(A):
        if a and cmb_e == 0:
            is1 = not is1
        cmb_e += contains(D-1-i) - contains(i+1)
    return is1

B = [abs(A[i]-A[i+1]) for i in range(N-1)]
if 1 in set(B):
    C = [b%2 for b in B]
    is1 = solve1(C, N-1)
    print(1 if is1 else 0)
else:
    C = [b//2 for b in B]
    is2 = solve1(C, N-1)
    print(2 if is2 else 0)