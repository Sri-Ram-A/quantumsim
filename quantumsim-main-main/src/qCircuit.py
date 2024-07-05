import qBit
import qGate

class QuantumCircuit:
    def __init__(self, gates):
        self.gates = gates

    def apply(self, qbit):
        for gate in self.gate:
            gate.apply(qbit)
