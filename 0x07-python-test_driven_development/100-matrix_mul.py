#!/usr/bin/python3
"""This is a matrix multiplication function."""


def matrix_mul(m_m, m_n):
    """Multiply two matrices.

    Args:
        m_m (list of lists of ints/floats): The first matrix.
        m_n (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_m or m_n is not a list of lists of ints/floats.
        TypeError: If either m_m or m_n is empty.
        TypeError: If either m_m or m_n has different-sized rows.
        ValueError: If m_m and m_n cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_m by m_n.
    """

    if m_m == [] or m_n == [[]]:
        raise ValueError("m_m can't be empty")
    if m_n == [] or m_n == [[]]:
        raise ValueError("m_n can't be empty")

    if not isinstance(m_m, list):
        raise TypeError("m_m must be a list")
    if not isinstance(m_n, list):
        raise TypeError("m_n must be a list")

    if not all(isinstance(row, list) for row in m_m):
        raise TypeError("m_m must be a list of lists")
    if not all(isinstance(row, list) for row in m_n):
        raise TypeError("m_n must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_m for num in row]):
        raise TypeError("m_m should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_n for num in row]):
        raise TypeError("m_n should contain only integers or floats")

    if not all(len(row) == len(m_m[0]) for row in m_m):
        raise TypeError("each row of m_m must should be of the same size")
    if not all(len(row) == len(m_n[0]) for row in m_n):
        raise TypeError("each row of m_n must should be of the same size")

    if len(m_m[0]) != len(m_n):
        raise ValueError("m_m and m_n can't be multiplied")

    inverted_b = []
    for r in range(len(m_n[0])):
        new_row = []
        for c in range(len(m_n)):
            new_row.append(m_n[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_m:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
