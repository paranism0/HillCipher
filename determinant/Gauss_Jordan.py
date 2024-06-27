import numpy as np


def determinant_gauss_jordan(m, n):
    # Convert the input matrix to a NumPy array
    mat = np.array(m, dtype=float)

    # Initialize the determinant as 1
    det = 1.0

    for i in range(n):
        # Find the maximum element in the current column
        max_row = i + np.argmax(np.abs(mat[i:, i]))

        # If the maximum element is 0, the determinant is 0
        if mat[max_row, i] == 0:
            return 0

        # Swap the current row with the row of the maximum element
        if i != max_row:
            mat[[i, max_row]] = mat[[max_row, i]]
            det *= -1  # Swapping rows changes the sign of the determinant

        # Multiply the determinant by the pivot element
        det *= mat[i, i]

        # Normalize the pivot row
        mat[i] /= mat[i, i]

        # Eliminate the current column elements below the pivot
        for j in range(i + 1, n):
            mat[j] -= mat[j, i] * mat[i]

    return det
