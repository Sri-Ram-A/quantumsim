import pStateVector
import numpy as np


class qBit:
    def __init__(self, state):
        if isinstance(state, pStateVector):
            self.state = state
        else:
            self.state = pStateVector(state)

    def measure(self):
        return self.state.measure()
