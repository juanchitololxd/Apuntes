import numpy as np


def isHermitian(vector):
    if vector.ndim == 2:
        if np.array_equal(vector, vector.transpose().conjugate()):
            return True
        return False


def isUnitary(matrix):
    if np.allclose(np.dot(matrix, matrix.transpose().conjugate()), np.identity(len(matrix))):
        return True
    return False


def eigenVectors(observable):
    return np.linalg.eig(observable)[1]
