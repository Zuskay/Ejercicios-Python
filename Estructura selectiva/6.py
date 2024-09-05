<<<<<<< HEAD
# Solicita al usuario que ingrese el promedio del alumno y lo convierte a un número flotante
promedioEstudiante = float(input("¿Cuál fue el promedio del alumno? "))

# Solicita al usuario que ingrese el valor de la pensión y lo convierte a un entero
pension = int(input("¿Cuál es el valor de la pensión $"))

# Verifica si el promedio del estudiante es mayor o igual a 4.0
if promedioEstudiante >= 4.0:
    # Si el promedio es 4.0 o mayor, se aplica un descuento del 30% sobre el valor de la pensión
    # Calcula el valor final de la pensión después de aplicar el descuento
    print(f"Obtienes un descuento del 30% sobre la pensión, por lo tanto el valor final de tu pensión es {int(pension - (pension * 0.3))}")
else:
    # Si el promedio es menor a 4.0, se aplica un IVA del 10% sobre el valor de la pensión
    iva = 0.1
    # Calcula el valor final de la pensión después de añadir el IVA
    print(f"El valor final de la pensión con IVA es {int(pension + (pension * iva))}")

=======
# Solicita al usuario que ingrese el promedio del alumno y lo convierte a un número flotante
promedioEstudiante = float(input("¿Cuál fue el promedio del alumno? "))

# Solicita al usuario que ingrese el valor de la pensión y lo convierte a un entero
pension = int(input("¿Cuál es el valor de la pensión $"))

# Verifica si el promedio del estudiante es mayor o igual a 4.0
if promedioEstudiante >= 4.0:
    # Si el promedio es 4.0 o mayor, se aplica un descuento del 30% sobre el valor de la pensión
    # Calcula el valor final de la pensión después de aplicar el descuento
    print(f"Obtienes un descuento del 30% sobre la pensión, por lo tanto el valor final de tu pensión es {int(pension - (pension * 0.3))}")
else:
    # Si el promedio es menor a 4.0, se aplica un IVA del 10% sobre el valor de la pensión
    iva = 0.1
    # Calcula el valor final de la pensión después de añadir el IVA
    print(f"El valor final de la pensión con IVA es {int(pension + (pension * iva))}")

>>>>>>> e202adae2eba232c5ee50d165221f050486cdf8d
