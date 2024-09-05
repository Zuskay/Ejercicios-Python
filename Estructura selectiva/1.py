# Solicita al usuario que ingrese la primera nota y la convierte a entero
nt = int(input("Digite la primera nota: "))

# Solicita al usuario que ingrese la segunda nota y la convierte a entero
nt2 = int(input("Digite la segunda nota: "))

# Solicita al usuario que ingrese la tercera nota y la convierte a entero
nt3 = int(input("Digite la tercera nota: "))

# Calcula el promedio de las tres notas
promedio = (nt + nt2 + nt3) / 3

# Verifica si el promedio es mayor o igual a 70
if promedio >= 70:
    # Si el promedio es 70 o más, imprime que el usuario aprobó
    print("Aprobaste")
else:
    # Si el promedio es menor a 70, imprime que el usuario no aprobó
    print("No Aprobó")
