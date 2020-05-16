A, B, C = map(int, input().split())

max = max([A,B,C])
print(sum([A,B,C])-max+max*10)