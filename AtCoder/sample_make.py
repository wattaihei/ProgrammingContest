import numpy as np

def grid(H, W, prob):
    with open('sample_grid.txt', 'w', encoding='utf-8') as f:
        f.write(str(H) + ' ' + str(W) + '\n')
        for _ in range(H):
            S = ''
            for _ in range(W):
                s = np.random.choice(['.', '#'], p=[1-prob, prob])
                S += s
            f.write(S + '\n')
    print('written')
        

def graph_ABC065D(N, max_xy):
    print(N)
    for _ in range(N):
        xi = np.random.randint(0, max_xy)
        yi = np.random.randint(0, max_xy)
        print(xi, yi)

def N_A(N, max_x):
    print(N)
    for _ in range(N):
        x = np.random.randint(0, max_x)
        print(x, end=' ')
    print()

if __name__ == "__main__":
    #grid(1000, 1000, 0.001)
    #graph_ABC065D(6, 10)
    N_A(8, 30)