A, B = map(int, input().split()) # 横に2個

if A <= 0 and 0 <= B:
    ans = 'Zero'
elif A > 0:
    ans = 'Positive'
elif (B - A) % 2 == 0:
    ans = 'Negative'
else:
    ans = 'Positive'

print(ans)
