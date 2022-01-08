from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import itertools
import numpy as np


##  The following ansatz is from p-VQD
def ansatz(parameter,n_spins,n_layer,entanglement_type='full', interaction_length=2,full_rotation='False',test_number=2):
    count = 0
    circuit = QuantumCircuit(n_spins)
    for j in range(n_layer):
        if (j%2==0):
            for i in range(n_spins):
                circuit.rx(parameter[count],i)
                count = count + 1
            circuit.barrier()
        if (j%2==1):
            for i in range(n_spins):
                circuit.ry(parameter[count],i)
                count = count + 1
            circuit.barrier()
        for i in range(n_spins-1):
            circuit.rzz(parameter[count],i,i+1)
            count = count + 1
        circuit.barrier()

    if (n_layer%2==1):
        for i in range(n_spins):
            circuit.ry(parameter[count],i)
            count = count + 1
    if (n_layer%2==0):
        for i in range(n_spins):
            circuit.rx(parameter[count],i)
            count = count + 1
    return circuit
