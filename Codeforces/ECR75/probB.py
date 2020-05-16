Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    Ss = [input() for _ in range(N)]
    Query.append((N, Ss))

for N, Ss in Query:
    NUM = [0, 0]
    even_odd = [0, 0]
    for S in Ss:
        even_odd[0] += S.count('0')
        even_odd[1] += S.count('1')
        NUM[len(S)%2] += 1
    if even_odd[0] % 2 == 1 and even_odd[1] % 2 == 1:
        if NUM[1]%2 == 0 and NUM[1]>=2:
            print(N)
        else:
            print(N-1)
    elif sum(even_odd)%2 == NUM[1]%2:
        print(N)
    else:
        print(N-1)