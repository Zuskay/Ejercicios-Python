# Inicializa las variables para calcular el promedio, la nota máxima y la nota mínima
promedio = 0
max = 0
min = 100

# Bucle que se repetirá 20 veces para ingresar las calificaciones de los estudiantes
for i in range(0, 20):
    # Solicita al usuario que ingrese una calificación, que se convierte a entero
    calificacion = int(input('Ingrese la calificacion de los estudiantes: '))
    
    # Acumula el total de las calificaciones divididas por 20 para calcular el promedio
    promedio += calificacion / 20
    
    # Actualiza la nota máxima si la calificación ingresada es mayor que la actual nota máxima
    if calificacion > max:
        max = calificacion
    # Actualiza la nota mínima si la calificación ingresada es menor que la actual nota mínima
    elif calificacion < min:
        min = calificacion

# Imprime la nota más alta, la nota más baja y el promedio de las calificaciones
print(f'La nota más alta es {max} \nLa nota más baja es {min} \nEl promedio es: {promedio}')
