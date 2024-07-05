import qBit
import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.op = matrix
        if not self.check_unitary():
            raise ValueError("Matrix is not unitary")

    def check_unitary(self):
        return np.allclose(np.eye(self.matrix.shape[0]), self.matrix.conj().T @ self.matrix)

    def apply(self, qbit):
        if isinstance(qbit, qBit):
            qbit.state = self.op @ qbit.state
        else:
            raise ValueError("Input must be a qBit object")