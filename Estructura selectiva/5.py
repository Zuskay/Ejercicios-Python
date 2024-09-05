# Solicita al usuario que ingrese su nombre y lo convierte a una cadena de texto
nombre = str(input("Digite su nombre "))

# Solicita al usuario que ingrese su sexo (masculino o femenino) y lo convierte a una cadena de texto
sexo = str(input("¿Es usted del sexo masculino o del femenino? "))

# Solicita al usuario que ingrese su edad y la convierte a un entero
edad = int(input("Digite su edad "))

# Calcula el número de pulsaciones recomendadas por cada 10 segundos de ejercicio aeróbico para hombres
fnpulsaciones = (220 - edad) / 10

# Calcula el número de pulsaciones recomendadas por cada 10 segundos de ejercicio aeróbico para mujeres
mnpulsaciones = (210 - edad) / 10

# Evalúa el sexo ingresado para determinar qué fórmula utilizar para el cálculo
if sexo == "masculino":
    # Si el sexo es masculino, muestra el número de pulsaciones recomendado usando la fórmula para hombres
    print(f"Señor {nombre}, el número de pulsaciones que usted debería tener por cada 10 seg de ejercicio aeróbico es: {mnpulsaciones}")
else:
    # Si el sexo no es masculino (asumido como femenino), muestra el número de pulsaciones recomendado usando la fórmula para mujeres
    print(f"Señora {nombre}, el número de pulsaciones que usted debería tener por cada 10 seg de ejercicio aeróbico es: {fnpulsaciones}")
