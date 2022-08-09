import numpy as np
from supportFunctions import *


def probabilityOnJ(ket, j):
    tmp_ket = ket.transpose()[0]
    ket_norm_squared = np.linalg.norm(tmp_ket) ** 2
    j_modulus = tmp_ket[j] * tmp_ket[j].conjugate()
    return j_modulus / ket_norm_squared


def transitionAmplitude(ket1, ket2):
    ket1 = ket1.copy().transpose()[0]
    ket2 = ket2.copy().transpose()[0]
    normalized_ket1 = ket1 / np.linalg.norm(ket1)
    normalized_ket2 = ket2 / np.linalg.norm(ket2)
    bra = normalized_ket2.transpose().conjugate()
    return np.dot(bra, normalized_ket1)


def expectedValue(observable, ket):
    if not isHermitian(observable):
        return None
    observed_ket = np.dot(observable, ket)
    bra = observed_ket.transpose().conjugate()
    return np.dot(bra, ket)


def variance(observable, ket):
    expected_value = expectedValue(observable, ket)
    delta = observable - (expected_value * np.identity(len(observable)))
    delta2 = np.linalg.matrix_power(delta, 2)
    return expectedValue(delta2, ket)


def eignValues(observable):
    return np.linalg.eigvals(observable)


def transitionafterObservation(observable, ket, eigenvector):
    eigen_vectors = eigenVectors(observable)
    if eigenvector > len(eigen_vectors):
        return None
    transposed_vector = np.array([eigen_vectors[eigenvector]])
    transposed_vector = transposed_vector.transpose()
    return transitionAmplitude(ket, transposed_vector) * transitionAmplitude(ket, transposed_vector).conjugate()


def dynamics(dynamic_matrices, ket):
    for i in range(len(dynamic_matrices)):
        ket = np.dot(dynamic_matrices[i], ket)
    return ket
