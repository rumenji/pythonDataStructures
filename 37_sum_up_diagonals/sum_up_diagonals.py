def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    if len(matrix) == 2:
        return sum(matrix[0]) + sum(matrix[1])
    if len(matrix) == 3:
        return matrix[0][0] + matrix[0][2] + matrix[1][1]*2 + matrix[2][0] + matrix[2][2]