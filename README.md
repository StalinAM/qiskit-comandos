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
