import time 
# Para poder medir el tiempo que tarda el código
import numpy as np 
# Para usar las herramientas de numpy

# Guardamos la cantidad de datos que vamos a usar
N = 8000000

print(f" INICIO DE PRUEBA CON {N:,} ELEMENTOS ")

# 1. PRIMERA PRUEBA: CON UNA LISTA NORMAL
# --------------------------------------------------

# Creamos la lista con los números ordenados
lista = list(range(N))

# Guardamos el momento exacto en el que empieza a correr el tiempo
inicio_lista = time.perf_counter() 

# Multiplicamos cada número de la lista por dos
lista_resultado = [x * 2 for x in lista]

# Guardamos el momento exacto en el que termina el proceso
fin_lista = time.perf_counter()

# Restamos los dos tiempos para saber el total que tardó
tiempo_lista = fin_lista - inicio_lista
print(f"Tiempo con Listas: {tiempo_lista:.4f} segundos") 


# 2. SEGUNDA PRUEBA: CON NUMPY
# --------------------------------------------------

# Creamos un bloque de números igual al anterior pero con numpy
array_np = np.arange(N)

# Volvemos a registrar el tiempo de inicio
inicio_array = time.perf_counter()

# Multiplicamos todo el bloque por dos al mismo tiempo
array_resultado = array_np * 2

# Registramos el tiempo en el que termina esta parte
fin_array = time.perf_counter()

# Sacamos la cuenta de cuánto tardó esta segunda prueba
tiempo_array = fin_array - inicio_array
print(f"Tiempo con Arrays (NumPy): {tiempo_array:.4f} segundos") 


# 3. RESULTADO FINAL
# --------------------------------------------------

# Comparamos los dos resultados para ver cuál fue más rápido
diferencia = tiempo_lista / tiempo_array
print(f"\nEl array fue aproximadamente {diferencia:.1f} veces mas rapido que la lista.")
