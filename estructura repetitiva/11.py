# Inicializamos contadores y acumuladores
hombres = 0              # Contador de hombres
mujeres = 0              # Contador de mujeres
alturas = 0             # Acumulador de alturas totales
alturaMayor = 0         # Contador de personas con altura mayor a 1.70 metros
alturaMenor = 0         # Contador de personas con altura menor o igual a 1.50 metros
numAlturas = 0          # Contador de entradas de altura

while True:
    # Solicita la edad del usuario
    edad = int(input('Digite su edad (o 0 para terminar): '))
    
    # Si la edad es 0, salimos del bucle
    if edad == 0:
        break
    
    # Solicita el sexo del usuario y lo convierte a minúsculas para estandarizar la comparación
    sex = input('Digite su sexo (masculino/femenino): ').lower()
    
    # Incrementa los contadores de hombres o mujeres según el sexo ingresado
    if sex == "femenino":
        mujeres += 1
    elif sex == "masculino":
        hombres += 1
    else:
        print("Sexo inválido. Por favor, ingrese 'masculino' o 'femenino'.")
        continue  # Salta al siguiente ciclo si el sexo ingresado es inválido

    # Solicita la altura del usuario en metros
    altura = float(input("Digite su altura en metros: "))
    
    # Acumula la altura total y aumenta el contador de alturas
    alturas += altura
    numAlturas += 1
    
    # Contadores de altura por rangos
    if altura > 1.70:
        alturaMayor += 1
    elif altura <= 1.50:
        alturaMenor += 1

# Calcula el promedio de altura si hay datos de altura
if numAlturas > 0:
    promedioAltura = alturas / numAlturas
    print(f"La cantidad de hombres es: {hombres}")
    print(f"La cantidad de mujeres es: {mujeres}")
    print(f"La altura promedio es: {promedioAltura:.2f} metros")
    print(f"Cantidad de personas con altura mayor a 1.70 metros: {alturaMayor}")
    print(f"Cantidad de personas con altura menor o igual a 1.50 metros: {alturaMenor}")
else:
    print("No se ingresaron datos de altura.")
