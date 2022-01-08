import numpy as np
from qiskit.quantum_info import Pauli
from qiskit.opflow		  import PauliOp, SummedOp

def generate_pauli(idx_x,idx_z,n):
    xmask = [0] * n
    zmask = [0] * n
    for i in idx_x: xmask[i] = 1
    for i in idx_z: zmask[i] = 1
    a_x = np.asarray(xmask, dtype=bool)
    a_z = np.asarray(zmask, dtype=bool)
    return Pauli((a_z, a_x))

def generate_XYZ(J_x,J_y,J_z,field,n_spins=3, pbc=True):
    int_x_list = []
    int_y_list = []
    int_z_list = []
    field_list = []
    if pbc:
        int_z_list.append(generate_pauli([], [0, n_spins - 1], n_spins))
        int_x_list.append(generate_pauli([0, n_spins - 1], [], n_spins))
        int_y_list.append(generate_pauli([0, n_spins - 1], [0, n_spins - 1], n_spins))
    for i in range(n_spins - 1):
        int_z_list.append(generate_pauli([], [i, i + 1], n_spins))
    for i in range(n_spins - 1):
        int_x_list.append(generate_pauli([i, i + 1], [], n_spins))
    for i in range(n_spins - 1):
        int_y_list.append(generate_pauli([i, i + 1], [i, i + 1], n_spins))
    for i in range(n_spins):
        field_list.append(generate_pauli([i], [], n_spins))
    int_x_coeff = [J_x] * len(int_x_list)
    int_y_coeff = [J_y] * len(int_y_list)
    int_z_coeff = [J_z] * len(int_z_list)
    field_coeff = [field] * len(field_list)
    H = PauliOp(int_x_list[0], int_x_coeff[0])
    for i in range(1, len(int_x_list)):
        H = H + PauliOp(int_x_list[i], int_x_coeff[i])
    for i in range(0, len(int_y_list)):
        H = H + PauliOp(int_y_list[i], int_y_coeff[i])
    for i in range(0, len(int_z_list)):
        H = H + PauliOp(int_z_list[i], int_z_coeff[i])

    for i in range(len(field_list)):
        H = H + PauliOp(field_list[i], field_coeff[i])
    return H
