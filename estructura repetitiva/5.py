# Inicializa las variables para almacenar la suma de pesos y la cantidad de personas en cada grupo de edad.
pesoNiño = 0
pesoJoven = 0
pesoAdulto = 0
pesoAnciano = 0

# Inicializa las variables para contar el número de personas en cada grupo de edad.
niños = 0
jovenes = 0
adultos = 0
ancianos = 0

# Inicializa las variables para calcular el promedio del peso en cada grupo de edad.
promedioNiños = 0
promedioJovenes = 0
promedioAdultos = 0
promedioAncianos = 0

# Empieza un bucle que se repetirá 50 veces (de 1 a 50) para recoger información sobre 50 personas.
for i in range(1, 51):
    # Solicita al usuario que ingrese la edad de una persona.
    edades = int(input('Ingresa tu edad: '))
    # Solicita al usuario que ingrese el peso de la persona.
    pesos = int(input('Ingresa tu peso: '))

    # Clasifica a la persona en un grupo de edad y actualiza el conteo y la suma de pesos correspondiente.
    if 0 <= edades <= 12: 
        # Si la edad está en el rango de 0 a 12 años (inclusive), se incrementa el conteo de niños y se suma el peso al total.
        niños += 1
        pesoNiño += pesos
        # Calcula el promedio de peso para el grupo de niños.
        promedioNiños = pesoNiño / niños
    elif 13 <= edades <= 29:
        # Si la edad está en el rango de 13 a 29 años (inclusive), se incrementa el conteo de jóvenes y se suma el peso al total.
        jovenes += 1
        pesoJoven += pesos
        # Calcula el promedio de peso para el grupo de jóvenes.
        promedioJovenes = pesoJoven / jovenes
    elif 30 <= edades <= 59:
        # Si la edad está en el rango de 30 a 59 años (inclusive), se incrementa el conteo de adultos y se suma el peso al total.
        adultos += 1
        pesoAdulto += pesos
        # Calcula el promedio de peso para el grupo de adultos.
        promedioAdultos = pesoAdulto / adultos
    elif edades >= 60:
        # Si la edad es 60 años o más, se incrementa el conteo de ancianos y se suma el peso al total.
        ancianos += 1
        pesoAnciano += pesos
        # Calcula el promedio de peso para el grupo de ancianos.
        promedioAncianos = pesoAnciano / ancianos
    else: 
        # Si la edad no está en ninguno de los rangos especificados, se muestra un mensaje de error.
        print('Digito erroneo')

# Muestra los promedios de peso para cada grupo de edad. Los promedios se redondean usando round() para facilitar la lectura.
print(f'El promedio del peso de los niños es: {round(promedioNiños)} \n El promedio del peso de los jóvenes es: {round(promedioJovenes)} \n El promedio del peso de los adultos es: {round(promedioAdultos)} \n El promedio del peso de los ancianos es: {round(promedioAncianos)}')
