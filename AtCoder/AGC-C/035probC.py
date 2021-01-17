import sys
input = sys.stdin.buffer.readline

N = int(input())

if bin(N).count("1") == 1:
    print("No")
else:
    print("Yes")
    Edges = []
    if N%4 == 3:
        for i in range(1, N):
            Edges.append((i, i+1))
            Edges.append((N+i, N+i+1))
        Edges.append((N, N+1))
    elif N%4 == 1:
        for i in range(2, N):
            Edges.append((i, i+1))
            Edges.append((i+N, i+1+N))
        Edges.append((N, N+2))
        Edges.append((1, 2))
        Edges.append((3, 1+N))
    elif N%4 == 2:
        for i in range(3, N-2):
            Edges.append((i, i+1))
            Edges.append((i+N, i+1+N))
        Edges.append((2, N-1))
        Edges.append((2+N, 2*N-1))
        Edges.append((N-1, 3))
        Edges.append((2*N-1, 3+N))
        Edges.append((N-2, 2+N))
        Edges.append((1, N))
        Edges.append((N, 2))
        Edges.append((N-1, N+1))
        Edges.append((N+1, 2*N))
    else:
        a = 1<<(len(bin(N))-3)
        b = N - a
        P = [a, b]
        for i in range(1, N):
            if i != a and i != b:
                P.append(i)
        for a0, a1 in zip(P, P[1:]):
            Edges.append((a0, a1))
            Edges.append((a0+N, a1+N))
        Edges.append((P[-1], P[0]+N))
        Edges.append((N, a))
        Edges.append((b, 2*N))
    
    # print(len(Edges))
    for p0, p1 in Edges:
        print(p0, p1)
