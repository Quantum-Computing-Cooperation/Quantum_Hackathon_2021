from energy import *
from gradient import *
from overlap import *
import numpy as np

def next_level(n_qubits,n_layer,op,ansatz,parameters,shots,instance, lr, n_reps):
    #curr_params = parameters[:][-1]
    length = n_layer*3*n_qubits
    curr_params   = np.random.rand(length)
    a = 15
    delta = 0.001
    length = len(parameters[0])
    level = len(parameters)
    a = 15
    for i in range(n_reps):
        nrj = energy(n_qubits,n_layer,op,ansatz,curr_params,shots,instance)
        cost = nrj[0]
        for lev in range(level):
            cost = cost + a*overlap(ansatz,parameters[:][lev],curr_params,instance,n_qubits,n_layer)
        grad = gradient(n_qubits, n_layer, op, ansatz, curr_params, shots, instance)
        for j in range(length):
            for lev in range(level):
                grad[j,0] = grad[j,0] + a/2/delta*(overlap(ansatz,parameters[:][lev],curr_params + delta*ei(j,length),instance,n_qubits,n_layer) - overlap(ansatz,parameters[:][lev],curr_params - delta*ei(j,length),instance,n_qubits,n_layer))
        curr_params = curr_params - lr*grad[:, 0]
        if i % 10 == 0:
            print('Run number: ', i + 1)
            print('Energy:', cost)
    print('=========================')
    print('Level n = ', level)
    print('Final Energy:', nrj[0])
    print('========================= \n')
    parameters.append(curr_params)
    return parameters
