# (x0, y0) of ax + by = 1
def oneOfSolution(a, b):
    if b == 1:
        return 0, 1
    d = a//b
    p, q = oneOfSolution(b, a%b)
    return q, p-d*q

