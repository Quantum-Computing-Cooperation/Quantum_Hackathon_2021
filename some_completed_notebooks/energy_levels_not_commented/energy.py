import qiskit
import numpy as np

from qiskit.opflow.state_fns           import CircuitStateFn, StateFn
from qiskit.opflow.expectations        import PauliExpectation
from qiskit.opflow.converters          import CircuitSampler

def energy(n_qubits, n_layer, op, ansatz, params, shots, instance):
    # Make the operator measurable
    op = StateFn(op, is_measurement=True)

    # create the wavefunction
    wfn = CircuitStateFn(ansatz(parameter=params, n_spins=n_qubits, n_layer=n_layer, full_rotation=True))
    opwfn = op @ wfn  # matrix product

    # Simulate the sampling
    grouped = PauliExpectation().convert(opwfn)
    sampled_op = CircuitSampler(instance).convert(grouped)

    # Expectation value
    mean_value = sampled_op.eval().real
    est_err = 0

    # If the simulations is not unitary evolution, return an error bar
    if (not instance.is_statevector):
        variance = PauliExpectation().compute_variance(sampled_op).real
        est_err = np.sqrt(variance / shots)

    return mean_value, est_err