from qiskit.opflow             import StateFn
from qiskit.opflow        import PauliExpectation
from qiskit.opflow        import CircuitSampler
import numpy as np

def projector_zero(n_qubits):
    from qiskit.opflow import I, X, Y, Z
    prj = (I + Z)
    for a in range(n_qubits - 1):
        prj = prj ^ (I + Z)
    prj = prj/np.power(2,n_qubits)
    return prj

def overlap(ansatz,param0,paramf,instance,n_qubits, n_layer):
    zero_proj = StateFn(projector_zero(n_qubits),is_measurement=True)
    ground_state_circuit = ansatz(param0,n_qubits,n_layer)
    excited_state_circuit = ansatz(paramf,n_qubits,n_layer)
    state_wfn = zero_proj @ StateFn(ground_state_circuit + excited_state_circuit.inverse())
    grouped = PauliExpectation().convert(state_wfn)
    sampled_op = CircuitSampler(instance).convert(grouped)
    overl = sampled_op.eval().real
    return overl