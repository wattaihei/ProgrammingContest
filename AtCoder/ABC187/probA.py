A, B = map(int, input().rstrip().split())
sa = sum(map(int, list(str(A))))
sb = sum(map(int, list(str(B))))
print(max(sa, sb))