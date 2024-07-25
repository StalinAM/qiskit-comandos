
#Transformada de Fourier Discreta
import numpy as np
import time

def dft(x):
    """Compute the discrete Fourier transform of the 1D array x."""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Crear una muestra aleatoria
N = 1024
x = np.random.rand(N)

# Medir el tiempo de ejecución de la DFT
start_time = time.time()
dft_result = dft(x)
classical_time = time.time() - start_time

print("DFT execution time:", classical_time)
