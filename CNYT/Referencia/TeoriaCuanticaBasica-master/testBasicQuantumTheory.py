import unittest
from basicQuantumTheory import *
import numpy as np
from scipy import constants


class TestComplexVectorSpaceLibrary(unittest.TestCase):

    def testProbabilityOnJ(self):
        ket = np.array([[-3-1j], [-2j], [1j], [2]])
        j = 2
        self.assertTrue(probabilityOnJ(ket, j) == 0.05263157894736841)

    def testTransitionAmplitude(self):
        ket1 = np.array([[1], [-1j]])
        ket2 = np.array([[1j], [1]])
        self.assertTrue(np.isclose(transitionAmplitude(ket1, ket2) == -1j))

    def testExpectedValue(self):
        observable = np.array([[0, -1j], [1j, 0]])
        ket = np.array([[1/np.sqrt(2)], [1j/np.sqrt(2)]])
        self.assertTrue(np.isclose(expectedValue(observable, ket)[0][0], 1+0j))

    def testVariance(self):
        observable = np.array([[0, -1j], [1j, 0]])
        ket = np.array([[1 / np.sqrt(2)], [1j / np.sqrt(2)]])
        self.assertTrue(variance(observable, ket) == 0)

    def testEigenValues(self):
        matrix = np.array([[1, 2], [3, 2]])
        self.assertTrue(np.array_equal(eignValues(matrix), np.array([-1, 4])))

    def testTransitionAfterObservation(self):
        observable = np.array([[-1, -1j], [1j, 1]])
        ket = np.array([[1/2], [1/2]])
        eigenvector = 1
        self.assertTrue(np.isclose(transitionafterObservation(observable, ket, eigenvector), 0.5))

    def dynamics(self):
        dynamic_matrices = [np.array([[1j, 0], [0, 1j]]), np.array([[0, 1j], [-1j, 0]])]
        ket = np.array([[1/2], [1/2]])
        self.assertTrue(np.array_equal(dynamics(dynamic_matrices, ket), np.array([[-1/2], [1/2]])))

    # Pruebas de los ejercicios del libro
    def test_4_3_1(self):
        a = constants.hbar/2
        spin_x = np.array([[0, a], [a, 0]])
        # Los posibles estados que se puede pasar el sistema al medirlo son todos los multiplos de sus vectores propios
        self.assertTrue(np.array_equal(np.array([[1/np.sqrt(2), -1/np.sqrt(2)], [1/np.sqrt(2), 1/np.sqrt(2)]]), eigenVectors(spin_x)))

    def test4_3_2(self):
        a = constants.hbar / 2
        spin_x = np.array([[0, a], [a, 0]])
        ket = np.array([[1], [0]])
        eigenvalues, eigenvectors = np.linalg.eig(spin_x)
        first_column_eigenvetor = np.array([eigenvectors[0]]).transpose()
        second_column_eigenvetor = np.array([eigenvectors[1]]).transpose()
        p1 = transitionAmplitude(ket, first_column_eigenvetor) * transitionAmplitude(ket, first_column_eigenvetor).conjugate()
        p2 = transitionAmplitude(ket, second_column_eigenvetor) * transitionAmplitude(ket, second_column_eigenvetor).conjugate()
        self.assertTrue(np.array_equal(((p1 * eigenvalues[0]) + (p2 * eigenvalues[1])), expectedValue(spin_x, ket)[0][0]))

    def test4_4_1(self):
        u1 = np.array([[0, 1], [1, 0]])
        u2 = np.array([[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]])
        u3 = np.dot(u1, u2)
        self.assertTrue(isUnitary(u1) and isUnitary(u2) and isUnitary(u3))

    def test4_4_2(self):
        ket = np.array([[1], [0], [0], [0]])
        matrix_dynamics = np.array([[0, 1/np.sqrt(2), 1/np.sqrt(2), 0], [1j/np.sqrt(2), 0, 0, 1/np.sqrt(2)], [1/np.sqrt(2), 0, 0, 1j/np.sqrt(2)], [0, 1/np.sqrt(2), -1/np.sqrt(2), 0]])
        dynamic_sistem = [matrix_dynamics, matrix_dynamics, matrix_dynamics]
        final_state = dynamics(dynamic_sistem, ket)
        self.assertTrue(probabilityOnJ(final_state, 3) == 0)


if __name__ == '__main__':
    unittest.main()