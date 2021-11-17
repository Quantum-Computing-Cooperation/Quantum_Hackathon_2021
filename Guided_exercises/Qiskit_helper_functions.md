# Qiskit helper functions

This documents aims to direct you towards useful Qiskit builtin functions that could be of help in the realization of the exercises.

There are many subroutines that could be quite complex and that Qiskit embeds in very simple methods to use. However, the idea of the hackathon is to approach this complexity with simple examples, before understanding how to use those generic and useful Qiskit modules. 


## Expectation Value

Qiskit has a method to compute easily expectation values for Pauli operators: https://qiskit.org/documentation/stubs/qiskit.aqua.operators.expectations.PauliExpectation.html#qiskit.aqua.operators.expectations.PauliExpectation

## Unitary to circuit converter

Transpile a unitary to circuit. You can define a unitary using the Operator class (initializable with a List of Lists to build your matrix) and add the quantum circuit corresponding to this unitary by simply calling the method unitary of your QuantumCircuit instance. Info available here: https://qiskit.org/documentation/stubs/qiskit.circuit.QuantumCircuit.unitary.html#qiskit.circuit.QuantumCircuit.unitary

## Create a controlled version of a quantum gate

You can convert a quantum circuit instance to a Qiskit gate instance, and create a controlled gate out of it following the syntax presented here:
https://qiskit.org/documentation/stubs/qiskit.circuit.Gate.control.html#qiskit.circuit.Gate.control

You can then recover the corresponding quantum circuit from the new gate: https://qiskit.org/documentation/stubs/qiskit.circuit.ControlledGate.html#qiskit.circuit.ControlledGate

