#!/usr/bin/python3
""" a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        tmp = [1]
        for t in range(len(tr) - 1):
            tmp.append(tri[t] + tri[t + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
