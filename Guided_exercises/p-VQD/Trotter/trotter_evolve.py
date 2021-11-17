import qiskit
from qiskit import QuantumCircuit
from expectation_value import *
from qiskit.quantum_info import Pauli
from qiskit.opflow import PauliOp

def trotter_evolve(n_spins = 3, J = 1.4, h = 1., final_time = 1., delta_t = .01):
    M = int(final_time/delta_t)
    qc = QuantumCircuit(n_spins)
    for layer in range(M):
        for k in range(n_spins-1):
            qc.rzz(-2.*J*delta_t, k, k+1)
        for k in range(n_spins):
            qc.rx(-2.*h*delta_t, k)
    return qc

def mag(circuit, instance, direction = "X"):
    magnetization = 0.
    strings = [direction + 'II', 'I' + direction + 'I', 'II' + direction]
    for string in strings:
        pauliop = PauliOp(Pauli(string))
        magnetization += expectation_value(pauliop, circuit, instance)
    return magnetization / 3.


