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

### Crear un cubit y ver el estado forma local

```python
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1,1)
qc.measure(0, 0)
qc.draw('mpl')

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

result = simulator.run(compiled_circuit).result()

counts = result.get_counts(compiled_circuit)
print(counts)
```

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

### Puerta Pauli-Y (Y)

actúa como una combinación de operaciones de rotación en los ejes X e Y.

```python
qc = QuantumCircuit(1)  # Crear un circuito con un qubit
qc.y(0)  # Aplicar la puerta Pauli-Y al qubit 0
qc.draw('mpl')
```

## Conectar IBM online

- Librerias

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.visualization import plot_histogram
```

- Circuito

```python
example_circuit = QuantumCircuit(2)
example_circuit.cx(0, 1)
example_circuit.measure_all()
```

- Mandar al backend

```python
# Seleccionar el backend menos ocupado que no sea un simulador
backend = service.least_busy(operational=True, simulator=False)

# Transpilar el circuito para el backend seleccionado
compiled_circuit = transpile(example_circuit, backend)

# Crear un sampler para ejecutar el circuito en el backend seleccionado
sampler = Sampler(backend)

# Ejecutar el trabajo y obtener el resultado
job = sampler.run([compiled_circuit])
print(f"job id: {job.job_id()}")

# Esperar a que el trabajo termine y obtener los resultados
job_result = job.result()
print(job_result)
```

- Obtener los datos para graficar

```python
counts = job_result[0].data.meas.get_counts()
print(counts)
```

- Graficar

```python
plot_histogram(counts)
```
