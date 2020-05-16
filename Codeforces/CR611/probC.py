import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
P = [False]*(N+1)
Q = [False]*(N+1)
for i, a in enumerate(A):
    if a != 0:
        P[a] = True
        Q[i+1] = True

both = []
q_only = []
p_only = []
for n in range(1, N+1):
    if not P[n] and not Q[n]:
        both.append(n)
    elif not P[n]:
        p_only.append(n)
    elif not Q[n]:
        q_only.append(n)

if both:
    q_only += both
    p_only += both
    p_only = p_only[1:] + p_only[:1]

for p, q in zip(p_only, q_only):
    A[q-1] = p

print(*A)