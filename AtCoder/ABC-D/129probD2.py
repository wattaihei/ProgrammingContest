#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import time


def main():
    r, c = map(int, input().split())
    g = numpy.array([[1 if v == '.' else 0 for v in input().strip()] for _ in range(r)])
    g = numpy.array([g, g])
    t0 = time.time()

    for x in range(1, c):
        g[0, :, x] += g[0, :, x] * g[0, :, x - 1]

    for x in range(c - 2, -1, -1):
        g[0, :, x] = (g[0, :, x] != 0) * numpy.maximum(g[0, :, x], g[0, :, x + 1])

    for y in range(1, r):
        g[1, y] += g[1, y] * g[1, y - 1]

    for y in range(r - 2, -1, -1):
        g[1, y] = (g[1, y] != 0) * numpy.maximum(g[1, y], g[1, y + 1])

    g = g[0] + g[1]

    print(numpy.max(g) - 1)
    t1 = time.time()
    print(t1 - t0)


if __name__ == '__main__':
    main()
    

