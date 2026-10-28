import numpy as np

# 1. Creamos la lista con las calificaciones de 10 alumnos
notas = np.array([40, 79, 53, 88, 32, 71, 83, 47, 91, 48])

print(f"--- FASE 1: DATOS ORIGINALES ---")
print(f"Notas iniciales: {notas}")

# 2. Sacamos las primeras métricas para entender cómo le fue al grupo
promedio_inicial = np.mean(notas) # Suma todas las notas y las divide por el total
nota_max = np.max(notas)          # Busca la calificación más alta de la lista
nota_min = np.min(notas)          # Encuentra el puntaje más bajo de todos

print(f"\n--- FASE 2: ESTADÍSTICAS INICIALES ---")
print(f"Promedio del grupo: {promedio_inicial:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

# 3. Modificamos las notas que no alcanzaron el puntaje mínimo
# Le sumamos 10 puntos a los alumnos que sacaron menos de 50; los demás se quedan igual
notas_ajustadas = np.where(notas < 50, notas + 10, notas)

# Ponemos un tope para que ninguna calificación quede por encima de 100
notas_ajustadas = np.clip(notas_ajustadas, 0, 100)

print(f"\n--- FASE 3: APLICACIÓN DE CRITERIOS (Incentivo aplicado) ---")
print(f"Notas ajustadas: {notas_ajustadas}")

# 4. Volvemos a calcular el promedio con los nuevos cambios realizados
promedio_final = np.mean(notas_ajustadas)

print(f"\n--- FASE 4: CONSOLIDACIÓN FINAL ---")
print(f"Promedio final del grupo tras ajustes: {promedio_final:.2f}")
print(f"Diferencia en el promedio: {promedio_final - promedio_inicial:+.2f} puntos")
