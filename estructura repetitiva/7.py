# Inicializa los contadores para cada color de carro en 0.
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0

# Inicializa el contador del número de carros procesados en 0.
i = 0

# Solicita al usuario que ingrese el número total de carros que entraron.
nCarros = int(input("Cuantos carros entraron: "))

# Inicia un bucle que continuará mientras el número de carros procesados (i) sea menor que el número total de carros (nCarros).
while i < nCarros:
    # Solicita al usuario que ingrese el último dígito de la placa del carro.
    placa = int(input("Ingresa el ultimo numero de tu placa: "))
    
    # Clasifica el carro en un color basado en el último dígito de la placa.
    if placa == 1 or placa == 2:
        # Si el dígito es 1 o 2, incrementa el contador de carros amarillos.
        amarillo += 1
    elif placa == 3 or placa == 4:
        # Si el dígito es 3 o 4, incrementa el contador de carros rosas.
        rosa += 1
    elif placa == 5 or placa == 6:
        # Si el dígito es 5 o 6, incrementa el contador de carros rojos.
        roja += 1
    elif placa == 7 or placa == 8:
        # Si el dígito es 7 o 8, incrementa el contador de carros verdes.
        verde += 1
    elif placa == 9 or placa == 0:
        # Si el dígito es 9 o 0, incrementa el contador de carros azules.
        azul += 1
    else:
        # Si el dígito no está en el rango de 0 a 9, muestra un mensaje de error.
        print("Digito incorrecto, debe ser un numero de 0 al 9")
    
    # Incrementa el contador de carros procesados.
    i += 1

# Imprime la cantidad de carros de cada color.
print(f'La cantidad de carros amarillos es: {amarillo} \n La cantidad de carros rosas es: {rosa} \n La cantidad de carros rojos es: {roja} \n La cantidad de carros verdes: {verde} \n La cantidad de carros azules es: {azul}')