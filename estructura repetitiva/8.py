# Inicializamos cuatro variables para contar el número de estudiantes en cada rango de calificaciones.
est1 = 0  # Contador para calificaciones menores a 50
est2 = 0  # Contador para calificaciones entre 50 y 69
est3 = 0  # Contador para calificaciones entre 70 y 79
est4 = 0  # Contador para calificaciones de 80 o más

# Bucle para procesar las calificaciones de 23 estudiantes
for estudiante in range(0, 23):  # Se repite 23 veces, una vez por cada estudiante
    # Se solicita al usuario que ingrese la calificación del estudiante
    nota = int(input('¿Cual fue tu calificacion del 1 al 100? '))
    
    # Se clasifica la calificación en uno de los cuatro rangos
    if nota < 50:
        est1 += 1  # Si la calificación es menor a 50, se incrementa el contador est1
    elif nota >= 50 and nota < 70:
        est2 += 1  # Si la calificación está entre 50 y 69, se incrementa el contador est2
    elif nota >= 70 and nota < 80:
        est3 += 1  # Si la calificación está entre 70 y 79, se incrementa el contador est3
    elif nota >= 80:
        est4 += 1  # Si la calificación es 80 o mayor, se incrementa el contador est4

# Imprimimos los resultados finales
print(f'Los estudiantes con una calificacion menor a 50 son: {est1} \n'
      f'Los estudiantes con una calificacion de 50 o mas pero menor que 70 son: {est2} \n'
      f'Los estudiantes con una calificaciones de 70 o mas pero menor que 80 son: {est3} \n'
      f'Los estudiantes con una calificacion de 80 o mas son: {est4}')
