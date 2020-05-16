L = int(input())
l = L.bit_length()

graph = []
for i in range(l-1):
    graph.append((i+1, i+2, 0))
    graph.append((i+1, i+2, 2**(l-i-2)))

s = (1 << (l-1))
for i in reversed(range(l-1)):
    if (1 << i) & L:
        graph.append((1, l-i, s))
        s += (1 << i)

print(l, len(graph))
for a, b, c in graph:
    print(a, b, c)