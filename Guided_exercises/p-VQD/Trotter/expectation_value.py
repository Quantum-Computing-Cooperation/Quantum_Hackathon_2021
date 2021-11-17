from qiskit.opflow.state_fns           import CircuitStateFn, StateFn
from qiskit.opflow.expectations        import PauliExpectation
from qiskit.opflow.converters          import CircuitSampler

def expectation_value(op, circuit, instance):
    op = StateFn(op, is_measurement=True)
    wfn = CircuitStateFn(circuit)
    opwfn = op @ wfn
    grouped = PauliExpectation().convert(opwfn)
    sampled_op = CircuitSampler(instance).convert(grouped)
    mean_value = sampled_op.eval().real
    return mean_value