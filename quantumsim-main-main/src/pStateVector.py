import numpy as np

class pStateVector:
    def __init__(self, state):
        self.state = np.array(state, dtype=complex)
        self.normalize()

    def normalize(self):
        norm = np.linalg.norm(self.state)
        if norm != 0:
            self.state /= norm

    def measure(self):
        probabilities = np.abs(self.state) ** 2
        return np.random.choice(len(self.state), p=probabilities)
