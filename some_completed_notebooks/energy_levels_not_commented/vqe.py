from energy import *
from gradient import *

def VQE(n_qubits, n_layer, op, ansatz, params, shots, instance, lr, n_reps):
    log = {}
    log['energies'] = []
    log['err_energies'] = []
    log['gradients'] = []

    curr_params = params
    file_energy = open("energies.txt","a+")
    for i in range(n_reps):
        # Measure energy and save it

        E = energy(n_qubits, n_layer, op, ansatz, curr_params, shots, instance)
        if i % 10 == 0:
            print('Run number: ', i + 1)
            print('Energy:', E[0])
            print('========================= \n')
        log['energies'].append(E[0])
        log['err_energies'].append(E[1])

        # Measure gradients
        g = gradient(n_qubits, n_layer, op, ansatz, curr_params, shots, instance)

        log['gradients'].append(g[:, 0])
        #         print(g)

        # Update parameters

        curr_params = curr_params - lr * g[:, 0]
        
        # Write in file

        file_energy.write(str(E[0])+' \n')
    file_energy.close()
                   
    log['curr_params'] = curr_params
    return log