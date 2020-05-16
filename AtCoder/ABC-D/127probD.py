N, M = map(int, input().split())
A = list(map(int, input().split()))

get = []
for _ in range(M):
    b, c = map(int, input().split())
    get += [c]*b
A = sorted(A)
get = sorted(get, reverse=True)
i_max = min([N, len(get)])

for i in range(i_max):
    sep = i
    if A[i] > get[i]:
        break
if sep == N - 1:
    replaced = get[:N]
elif sep == len(get) - 1:
    replaced = get + A[sep:]
else:
    replaced = get[:sep] + A[sep:]
print(sum(replaced))