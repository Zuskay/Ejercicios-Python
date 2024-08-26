# Solicita al usuario que ingrese el monto total de la compra y lo convierte a un entero
mtotal = int(input("Ingrese el monto total de la compra: "))

# Verifica si el monto total es mayor a 500,000
if mtotal > 500000:
    # Calcula el porcentaje de la inversión de la empresa (55% del monto total)
    inver = int((mtotal * 55) / 100)
    
    # Calcula el porcentaje del monto pedido prestado al banco (30% del monto total)
    pres = int((mtotal * 30) / 100)
    
    # Calcula el porcentaje del crédito solicitado al fabricante (15% del monto total)
    credito = int((mtotal * 15) / 100)
    
    # Muestra el dinero invertido por la empresa, el dinero pedido prestado al banco y el crédito solicitado al fabricante
    print(f"El dinero invertido de la empresa es: {inver} \nEl dinero que se pidió prestado al banco es: {pres} \nY el dinero del crédito solicitado al fabricante es {credito}")
else:
    # Calcula el porcentaje de la inversión de la empresa (70% del monto total)
    inver = int((mtotal * 70) / 100)
    
    # Calcula el porcentaje del crédito solicitado al fabricante (30% del monto total)
    credito = int(((mtotal * 30) / 100))
    
    # Calcula el monto total del crédito incluyendo un interés del 20%
    intereses = int((credito * 0.2) + credito)
    
    # Muestra el dinero invertido por la empresa y el crédito solicitado al fabricante (con interés incluido)
    print(f"El dinero invertido de la empresa es: {inver}\nEl crédito solicitado al fabricante es de {intereses}")
