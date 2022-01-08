from qiskit.opflow.state_fns           import CircuitStateFn, StateFn
from qiskit.opflow.expectations        import PauliExpectation
from qiskit.opflow.converters          import CircuitSampler
import numpy as np

def ei(i, n):
    vi = np.zeros(n)
    vi[i] = 1.0
    return vi[:]


def gradient(n_qubits, n_layer, op, ansatz, params, shots, instance):
    n_params = len(params)
    wfn_circuits = []
    op = StateFn(op, is_measurement=True)

    for i in range(n_params):
        wfn_circuits.append(CircuitStateFn(
            ansatz(params + ei(i, n_params) * np.pi / 2.0, n_spins=n_qubits, n_layer=n_layer, full_rotation=True)))
        wfn_circuits.append(CircuitStateFn(
            ansatz(params - ei(i, n_params) * np.pi / 2.0, n_spins=n_qubits, n_layer=n_layer, full_rotation=True)))

    # Now measure circuits
    results = []
    for wfn in wfn_circuits:
        braket = op @ wfn

        # Simulate the sampling
        grouped = PauliExpectation().convert(braket)
        sampled_op = CircuitSampler(instance).convert(grouped)

        # Expectation value
        mean_value = sampled_op.eval().real
        est_err = 0

        # If the simulations is not unitary evolution, return an error bar
        if (not instance.is_statevector):
            variance = PauliExpectation().compute_variance(sampled_op).real
            est_err = np.sqrt(variance / shots)

        results.append([mean_value, est_err])

    g = np.zeros((n_params, 2))
    for i in range(n_params):
        rplus = results[2 * i]
        rminus = results[2 * i + 1]
        # G      = (Ep - Em)/2
        # var(G) = var(Ep) * (dG/dEp)**2 + var(Em) * (dG/dEm)**2
        g[i, :] = (rplus[0] - rminus[0]) / 2.0, np.sqrt(rplus[1] ** 2 + rminus[1] ** 2) / 2.0

    return g