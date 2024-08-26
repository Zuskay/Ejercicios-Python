# Solicita al usuario que ingrese la cantidad de zapatillas compradas y la convierte a entero
zap = int(input("Cuántas zapatillas compró: "))

# Calcula el valor total de la compra sin descuento (suponiendo que cada zapatilla cuesta 50,000)
valorZap = zap * 50000

# Verifica si la cantidad de zapatillas es 3 o más
if zap >= 3:
    # Calcula el descuento del 20% para compras de 3 o más zapatillas
    desc = int(valorZap * 0.2)
    # Imprime el valor total de la compra antes del descuento
    print(f"El valor de la compra es de {valorZap}")
    # Imprime el monto del descuento y menciona el ahorro
    print(f"Le daremos un descuento del 20% por comprar 3 o más zapatillas, se ahorrará: {desc}")
    # Calcula el valor final después de aplicar el descuento
    valorZap = int(valorZap - desc)
    # Imprime el valor final de la compra con el descuento aplicado
    print(f"El valor final de la compra con el descuento agregado es {valorZap}")
else:
    # Calcula el descuento del 10% para compras de menos de 3 zapatillas
    desc = int(valorZap * 0.1)
    # Imprime el valor total de la compra antes del descuento
    print(f"El valor de la compra es de {valorZap}")
    # Imprime el monto del descuento y menciona el ahorro
    print(f"Le daremos un descuento del 10% por comprar menos de 3 zapatillas, se ahorrará: {desc}")
    # Calcula el valor final después de aplicar el descuento
    valorZap = int(valorZap - desc)
    # Imprime el valor final de la compra con el descuento aplicado
    print(f"El valor final de la compra con el descuento agregado es {valorZap}")
