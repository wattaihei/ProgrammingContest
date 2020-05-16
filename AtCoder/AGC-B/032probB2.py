N = int(input())

def main():
    graph = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i+j == N//2*2+1:
                continue
            graph.append([i, j])
    print(len(graph))
    for i, j in graph:
        print(i, j)

if __name__ == "__main__":
    main()