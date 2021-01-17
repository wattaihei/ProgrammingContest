
if __name__ == "__main__":
    
    from numpy.fft import rfft, irfft
    import numpy as np

    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().rstrip().split()))

    P = 200003
    P = 13

    twoind_to_val = [0]*P
    val_to_twoind = [0]*P

    b = 1
    for ind in range(P):
        twoind_to_val[ind] = b
        val_to_twoind[b] = ind
        b = b * 2 % P

    V = [0]*P
    for a in A:
        if a == 0: continue
        V[val_to_twoind[a]] += 1

    V = np.array(V)
    fft_len = 2*P+3

    AA = rfft(V, fft_len)
    BB = rfft(V, fft_len)
    X = (irfft(AA*BB)[:2*P]+0.5).astype(int)

    ans = 0
    for i in range(2*P):
        ans += twoind_to_val[i%P] * X[i]
        if i%2 == 0:
            v = V[i//2]
            ans -= twoind_to_val[i%P] * v*(v-1)//2

    print(ans//2)