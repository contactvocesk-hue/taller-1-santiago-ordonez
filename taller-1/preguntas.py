# PREGUNTA #1
# ¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array,
# y a qué crees que se deben esas diferencias?

# RESPUESTA:
# NumPy le gana por muchísimo a la lista normal de Python. En la prueba con 8 millones de datos, la lista se toma varios 
# segundos haciendo todo el recorrido número por número, mientras que el array hace la multiplicación casi al instante.

# Causa: La lista normal obliga a Python a revisar y procesar cada elemento uno por uno de forma manual. En cambio, 
# NumPy hace trampa porque viene programado por dentro con lenguaje C, lo que le permite hacer las operaciones directamente 
# en el procesador y de un solo golpe, saltándose todo el trabajo lento que hace Python.


# PREGUNTA #2
# ¿Cómo influye la forma en que cada estructura almacena los datos en memoria en el rendimiento obtenido durante la ejecución?

# RESPUESTA:
# Lista nativa de Python: No guarda los números juntos, sino que guarda "direcciones" que apuntan a dónde están los números 
# regados por toda la memoria. Esto hace que la computadora pierda mucho tiempo saltando de un lado a otro para buscar 
# cada valor, lo que vuelve todo más lento.

# Array de NumPy: Guarda todos los números pegados, uno al lado del otro, en un solo bloque limpio de memoria y bajo el mismo 
# formato. Gracias a este orden, el procesador puede leer los datos en fila sin dar vueltas y aplicar superpoderes del hardware 
# para procesar paquetes enteros de números a la vez.


# PREGUNTA #3
# Si tuvieras que elegir una de estas estructuras para procesar grandes volúmenes de datos numéricos, ¿cuál seleccionarías y por qué?

# RESPUESTA:
# Me quedo con el array de NumPy sin dudarlo. 

# La razón es sencilla: no desperdicia espacio en la memoria y corre muchísimo más rápido cuando manejas millones de datos. 
# Usar listas comunes para trabajos grandes o pesados haría que cualquier programa de análisis de datos o inteligencia 
# artificial se vuelva lento, pesado y poco práctico en el mundo real.
