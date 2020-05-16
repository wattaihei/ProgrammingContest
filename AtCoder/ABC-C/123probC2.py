N = int(input())
City = [int(input()) for _ in range(5)]

city = min(City)
amari = N % city
b = N // city + 1 if amari != 0 else N // city

print(b+len(City)-1)