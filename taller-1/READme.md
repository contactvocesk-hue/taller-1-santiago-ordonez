# 📊 Taller de Algoritmos y Rendimiento con NumPy

Repositorio que contiene los ejercicios prácticos desarrollados para el taller, enfocados en el análisis de rendimiento de estructuras de datos y el procesamiento numérico vectorizado con Python y NumPy.

---

## 📂 Estructura del Proyecto

* **`Problema1.py`**: Script que realiza una prueba de rendimiento (*benchmark*) comparando los tiempos de ejecución entre listas nativas de Python y arrays de NumPy utilizando 8 millones de elementos.
* **`Problema1_Preguntas.py`**: Respuestas teóricas sobre el uso de memoria, almacenamiento y velocidad de procesamiento.
* **`Problema2.py`**: Script de procesamiento de notas utilizando operaciones vectorizadas (`np.mean`, `np.where`, `np.clip`) para aplicar incentivos y calcular estadísticas de un grupo de estudiantes de forma eficiente.

---

## 📝 Respuestas del Taller (Problema 1)

1. **¿Qué diferencias observas en el tiempo de ejecución al realizar la misma operación con una lista y con un array, y a qué crees que se deben esas diferencias?**
   
   NumPy le gana por muchísimo a la lista normal de Python. En la prueba con 8 millones de datos, la lista se toma varios segundos haciendo todo el recorrido número por número, mientras que el array hace la multiplicación casi al instante.
   
   *Causa:* La lista normal obliga a Python a revisar y procesar cada elemento uno por uno de forma manual. En cambio, NumPy hace trampa porque viene programado por dentro con lenguaje C, lo que le permite hacer las operaciones directamente en el procesador y de un solo golpe, saltándose todo el trabajo lento que hace Python.

2. **¿Cómo influye la forma en que cada estructura almacena los datos en memoria en el rendimiento obtenido durante la ejecución?**
   
   *Lista nativa de Python:* No guarda los números juntos, sino que guarda "direcciones" que apuntan a dónde están los números regados por toda la memoria. Esto hace que la computadora pierda mucho tiempo saltando de un lado a otro para buscar cada valor, lo que vuelve todo más lento.
   
   *Array de NumPy:* Guarda todos los números pegados, uno al lado del otro, en un solo bloque limpio de memoria y bajo el mismo formato. Gracias a este orden, el procesador puede leer los datos en fila sin dar vueltas y aplicar superpoderes del hardware para procesar paquetes enteros de números a la vez.

3. **Si tuvieras que elegir una de estas estructuras para procesar grandes volúmenes de datos numéricos, ¿cuál seleccionarías y por qué?**
   
   Me quedo con el array de NumPy sin dudarlo. La razón es sencilla: no desperdicia espacio en la memoria y corre muchísimo más rápido cuando manejas millones de datos. Usar listas comunes para trabajos grandes o pesados haría que cualquier programa de análisis de datos o inteligencia artificial se vuelva lento, pesado y poco práctico en el mundo real.

---

## 🖥️ Resultados de Ejecución

**Ejercicio 1: Comparativa de Rendimiento (Listas vs NumPy)**  
![Resultado Comparativa](assets/resultado_comparativa.png)

**Ejercicio 2: Procesamiento de Notas con NumPy**  
![Resultado Notas](assets/resultado_notas.png)
