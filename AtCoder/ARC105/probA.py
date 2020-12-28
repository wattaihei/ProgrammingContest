A, B, C, D = map(int, input().split())
ok = (A == B+C+D) or (B == A+C+D) or (C == A+B+D) or (D == A+C+B) or (A+B == C+D) or (A+C == B+D) or (A+D == C+B)
print("Yes" if ok else "No")