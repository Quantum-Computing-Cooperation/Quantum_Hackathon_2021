import qiskit
from qiskit import QuantumCircuit

def prepare(cir):
    tqubits = 3
    q1 = tqubits
    q2 = tqubits+1
    q3 = tqubits+2
    cir.h(q1)
    cir.ch(q1,q2)
    cir.cx(q2,q3)
    cir.x(q1)
    return cir