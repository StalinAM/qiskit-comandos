# Comandos para emulador qiskit

## Instalacion

- Descargar [Anaconda](https://www.anaconda.com/download)
- Abrir Anaconda Prompt
- `conda create --name cwq`
- `conda activate cwq`
- `conda install pip`
- `pip install qiskit`
- `pip install qiskit-ibm-runtime`
- `pip install qiskit[visualization]`
- `pip install jupyter`

- Abrir notebook
- `jupyter notebook`

## Transformada de Fourier Cuantica

```python
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import numpy as np
import time

def qft(n):
    """Creates a QFT circuit on n qubits."""
    qc = QuantumCircuit(n)
    for j in range(n):
        for k in range(j):
            qc.cp(np.pi / 2**(j - k), k, j)
        qc.h(j)
    return qc

# Number of qubits
n = 10
qft_circuit = qft(n)
qft_circuit.measure_all()

# Execute the QFT circuit on a simulator
backend = AerSimulator()
transpiled_qft = transpile(qft_circuit, backend)

start_time = time.time()
result = backend.run(transpiled_qft, shots=1024).result()
quantum_time = time.time() - start_time

counts = result.get_counts()
plot_histogram(counts)
print("QFT execution time:", quantum_time)
```

## Definiciones

### Puerta Hadamard (H)

La puerta Hadamard transforma un qubit de un estado base (|0⟩ o |1⟩) a una superposición de ambos estados.

```python
qc = QuantumCircuit(1)
qc.h(0)
qc.draw('mpl')
```

### Puerta CNOT (CX)

Es una puerta de dos qubits donde el segundo qubit (target) es invertido (NOT) si el primer qubit (control) es 1.

```python
qc = QuantumCircuit(2)  # Crear un circuito con dos qubits
qc.cx(0, 1)  # Aplicar la puerta CNOT con el qubit 0 como control y el qubit 1 como objetivo
qc.draw('mpl')
```

### Puerta Pauli-X (X)

es equivalente a la operación NOT en la computación clásica.

```python
qc = QuantumCircuit(1)  # Crear un circuito con un qubit
qc.x(0)  # Aplicar la puerta Pauli-X al qubit 0
qc.draw('mpl')
```

```python
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Crear un nuevo circuito cuántico con 1 qubit y 1 bit clásico
qc = QuantumCircuit(1, 1)

# Aplicar una puerta X para poner el qubit en el estado |1⟩
qc.x(0)

# Aplicar otra puerta X para revertir el qubit al estado |0⟩
qc.x(0)

# Medir el qubit y almacenar el resultado en el bit clásico
qc.measure(0, 0)

# Dibujar el circuito
qc.draw("mpl")

# Transpilar el circuito para el simulador Aer
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

# Ejecutar el circuito en el simulador
result = simulator.run(compiled_circuit).result()

# Obtener y mostrar los resultados
counts = result.get_counts(compiled_circuit)
print(counts)
```

### Puerta Pauli-Y (Y)

actúa como una combinación de operaciones de rotación en los ejes X e Y.

```python
qc = QuantumCircuit(1)  # Crear un circuito con un qubit
qc.y(0)  # Aplicar la puerta Pauli-Y al qubit 0
qc.draw('mpl')
```
